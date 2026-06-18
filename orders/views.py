import random, hashlib, hmac
from django.conf import settings
from django.core.cache import cache
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import requests as http_requests

from .models import Address, Order, OrderItem
from .serializers import AddressSerializer, OrderSerializer


# ── Address APIs ──────────────────────────────────────────

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def address_list_create(request):
    if request.method == 'GET':
        addresses = Address.objects.filter(user=request.user)
        return Response(AddressSerializer(addresses, many=True).data)

    serializer = AddressSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def address_detail(request, pk):
    try:
        address = Address.objects.get(pk=pk, user=request.user)
    except Address.DoesNotExist:
        return Response({'error': 'Address not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(AddressSerializer(address).data)
    if request.method == 'PUT':
        serializer = AddressSerializer(address, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        address.delete()
        return Response({'message': 'Address deleted.'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def set_default_address(request, pk):
    try:
        address = Address.objects.get(pk=pk, user=request.user)
    except Address.DoesNotExist:
        return Response({'error': 'Address not found.'}, status=status.HTTP_404_NOT_FOUND)
    address.is_default = True
    address.save()
    return Response({'message': 'Default address updated.'})


# ── OTP APIs ──────────────────────────────────────────────

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_otp(request):
    cache_key = f"checkout_otp_{request.user.id}"

    # ✅ KEY FIX: If a valid OTP already exists in cache, return the SAME one
    # This prevents double-call (React StrictMode) from generating two different OTPs
    existing_otp = cache.get(cache_key)
    if existing_otp:
        return Response({
            'message': 'OTP already sent.',
            'otp': existing_otp,   # Return same OTP — no confusion
            'expires_in': 120,
        })

    # Generate fresh OTP
    otp = str(random.randint(100000, 999999))
    cache.set(cache_key, otp, timeout=120)

    return Response({
        'message': 'OTP sent successfully.',
        'otp': otp,
        'expires_in': 120,
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def verify_otp(request):
    entered_otp = str(request.data.get('otp', '')).strip()
    cache_key   = f"checkout_otp_{request.user.id}"
    stored_otp  = cache.get(cache_key)

    if not stored_otp:
        return Response(
            {'error': 'OTP expired. Please request a new one.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    if entered_otp != str(stored_otp):
        return Response(
            {'error': 'Incorrect OTP. Please check and try again.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Mark verified for 10 minutes
    verified_key = f"checkout_verified_{request.user.id}"
    cache.set(verified_key, True, timeout=600)
    cache.delete(cache_key)
    return Response({'message': 'OTP verified successfully.', 'verified': True})


# ── Coupon API ────────────────────────────────────────────

COUPONS = {
    'MULTIMART10': {'discount_pct': 10, 'min_order': 500},
    'SAVE20':      {'discount_pct': 20, 'min_order': 1000},
    'FIRST50':     {'discount_pct': 50, 'min_order': 2000},
    'WELCOME15':   {'discount_pct': 15, 'min_order': 0},
}

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def apply_coupon(request):
    code   = request.data.get('code', '').strip().upper()
    amount = float(request.data.get('amount', 0))

    if code not in COUPONS:
        return Response({'error': 'Invalid coupon code.'}, status=status.HTTP_400_BAD_REQUEST)

    coupon = COUPONS[code]
    if amount < coupon['min_order']:
        return Response(
            {'error': f"Minimum order ₹{coupon['min_order']} required for this coupon."},
            status=status.HTTP_400_BAD_REQUEST
        )

    discount_amount = round(amount * coupon['discount_pct'] / 100, 2)
    return Response({
        'code': code,
        'discount_pct': coupon['discount_pct'],
        'discount_amount': discount_amount,
        'message': f"{coupon['discount_pct']}% discount applied!",
    })


# ── Order APIs ────────────────────────────────────────────

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order(request):
    data = request.data

    address_id = data.get('address_id')
    try:
        address = Address.objects.get(pk=address_id, user=request.user)
    except Address.DoesNotExist:
        return Response({'error': 'Please select a valid delivery address.'}, status=status.HTTP_400_BAD_REQUEST)

    payment_method = data.get('payment_method', 'cod')
    if payment_method != 'cod':
        verified_key = f"checkout_verified_{request.user.id}"
        if not cache.get(verified_key):
            return Response(
                {'error': 'OTP verification required before payment.'},
                status=status.HTTP_403_FORBIDDEN
            )

    cart_items = data.get('cart_items', [])
    subtotal   = float(data.get('subtotal', 0))
    discount   = float(data.get('discount', 0))
    delivery   = float(data.get('delivery_charge', 0))
    tax        = round(subtotal * 0.18 / 100, 2)
    total      = round(subtotal - discount + delivery + tax, 2)
    coupon_code = data.get('coupon_code', '')

    order = Order.objects.create(
        user=request.user,
        address=address,
        payment_method=payment_method,
        subtotal=subtotal,
        discount=discount,
        delivery_charge=delivery,
        tax=tax,
        total_amount=total,
        coupon_code=coupon_code,
        payment_status='pending',
        order_status='placed',
    )

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product_id=item.get('id', 0),
            product_name=item.get('productName', ''),
            img_url=item.get('imgUrl', ''),
            price=item.get('price', 0),
            quantity=item.get('qty', 1),
        )

    if payment_method == 'razorpay':
        try:
            rz_resp = http_requests.post(
                'https://api.razorpay.com/v1/orders',
                auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET),
                json={'amount': int(total * 100), 'currency': 'INR', 'payment_capture': 1},
                timeout=10,
            )
            rz_data = rz_resp.json()
            if rz_resp.status_code == 200:
                order.razorpay_order_id = rz_data['id']
                order.save()
                return Response({
                    'order_id': order.id,
                    'razorpay_order_id': rz_data['id'],
                    'razorpay_key': settings.RAZORPAY_KEY_ID,
                    'amount': int(total * 100),
                    'currency': 'INR',
                })
            else:
                order.delete()
                return Response(
                    {'error': rz_data.get('error', {}).get('description', 'Razorpay error')},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        except Exception as e:
            order.delete()
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({
        'order_id': order.id,
        'total': total,
        'payment_method': payment_method,
        'message': 'Order placed successfully!',
    }, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def confirm_payment(request):
    order_id   = request.data.get('order_id')
    rz_order   = request.data.get('razorpay_order_id')
    rz_payment = request.data.get('razorpay_payment_id')
    rz_sig     = request.data.get('razorpay_signature')

    try:
        order = Order.objects.get(pk=order_id, user=request.user)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found.'}, status=status.HTTP_404_NOT_FOUND)

    message  = f"{rz_order}|{rz_payment}"
    expected = hmac.new(
        settings.RAZORPAY_KEY_SECRET.encode(),
        message.encode(),
        hashlib.sha256,
    ).hexdigest()

    if expected != rz_sig:
        order.payment_status = 'failed'
        order.save()
        return Response({'error': 'Payment verification failed.'}, status=status.HTTP_400_BAD_REQUEST)

    order.payment_status      = 'paid'
    order.order_status        = 'confirmed'
    order.razorpay_payment_id = rz_payment
    order.save()
    cache.delete(f"checkout_verified_{request.user.id}")

    return Response({'message': 'Payment confirmed!', 'order_id': order.id, 'payment_id': rz_payment})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return Response(OrderSerializer(orders, many=True).data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_detail(request, pk):
    try:
        order = Order.objects.get(pk=pk, user=request.user)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found.'}, status=status.HTTP_404_NOT_FOUND)
    return Response(OrderSerializer(order).data)
