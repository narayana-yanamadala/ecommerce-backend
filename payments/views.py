import hmac
import hashlib
import requests
import json
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order(request):
    try:
        amount = request.data.get('amount')
        if not amount:
            return Response({'error': 'Amount is required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Convert to paise — must be integer, minimum 100 paise (₹1)
        amount_in_paise = int(float(str(amount))) * 100

        if amount_in_paise < 100:
            return Response({'error': 'Minimum order amount is ₹1.'}, status=status.HTTP_400_BAD_REQUEST)

        payload = {
            'amount': amount_in_paise,
            'currency': 'INR',
            'payment_capture': 1
        }

        response = requests.post(
            'https://api.razorpay.com/v1/orders',
            auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET),
            json=payload,
            timeout=10
        )

        order = response.json()

        if response.status_code != 200:
            error_desc = order.get('error', {}).get('description', 'Order creation failed.')
            error_code = order.get('error', {}).get('code', '')
            return Response(
                {'error': f'{error_desc} (Code: {error_code})'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response({
            'order_id': order['id'],
            'amount': order['amount'],
            'currency': order['currency'],
            'key': settings.RAZORPAY_KEY_ID,
        })

    except requests.exceptions.ConnectionError:
        return Response({'error': 'Cannot connect to Razorpay. Check your internet connection.'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    except Exception as e:
        return Response({'error': f'Server error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def verify_payment(request):
    try:
        order_id  = request.data.get('razorpay_order_id')
        payment_id = request.data.get('razorpay_payment_id')
        signature  = request.data.get('razorpay_signature')

        if not all([order_id, payment_id, signature]):
            return Response({'error': 'Missing payment details.'}, status=status.HTTP_400_BAD_REQUEST)

        message = f"{order_id}|{payment_id}"
        expected_signature = hmac.new(
            settings.RAZORPAY_KEY_SECRET.encode('utf-8'),
            message.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()

        if expected_signature == signature:
            return Response({
                'status': 'success',
                'message': 'Payment verified successfully!',
                'payment_id': payment_id,
                'order_id': order_id,
            })
        else:
            return Response({'error': 'Payment verification failed. Invalid signature.'}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'error': f'Verification error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
