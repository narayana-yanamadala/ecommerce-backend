from django.urls import path
from . import views

urlpatterns = [
    # Address
    path('addresses/',                views.address_list_create,  name='address-list-create'),
    path('addresses/<int:pk>/',       views.address_detail,       name='address-detail'),
    path('addresses/<int:pk>/default/', views.set_default_address, name='address-set-default'),

    # OTP
    path('otp/send/',    views.send_otp,    name='otp-send'),
    path('otp/verify/',  views.verify_otp,  name='otp-verify'),

    # Coupon
    path('coupon/apply/', views.apply_coupon, name='coupon-apply'),

    # Orders
    path('orders/',           views.order_list,   name='order-list'),
    path('orders/create/',    views.create_order, name='order-create'),
    path('orders/<int:pk>/',  views.order_detail, name='order-detail'),
    path('orders/confirm/',   views.confirm_payment, name='order-confirm'),
]
