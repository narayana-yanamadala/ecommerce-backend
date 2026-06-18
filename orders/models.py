from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    ADDRESS_TYPE_CHOICES = [('home', 'Home'), ('work', 'Work')]

    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    full_name   = models.CharField(max_length=150)
    phone       = models.CharField(max_length=15)
    street      = models.CharField(max_length=300)
    landmark    = models.CharField(max_length=200, blank=True)
    city        = models.CharField(max_length=100)
    state       = models.CharField(max_length=100)
    pincode     = models.CharField(max_length=10)
    address_type = models.CharField(max_length=10, choices=ADDRESS_TYPE_CHOICES, default='home')
    is_default  = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.is_default:
            Address.objects.filter(user=self.user, is_default=True).update(is_default=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} - {self.city}"

    class Meta:
        ordering = ['-is_default', '-created_at']


class Order(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('razorpay', 'Razorpay'),
        ('upi', 'UPI'),
        ('cod', 'Cash on Delivery'),
        ('wallet', 'Wallet'),
    ]
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]
    ORDER_STATUS_CHOICES = [
        ('placed', 'Placed'),
        ('confirmed', 'Confirmed'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    user            = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    address         = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    payment_method  = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    subtotal        = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    discount        = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    delivery_charge = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    tax             = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_amount    = models.DecimalField(max_digits=12, decimal_places=2)
    coupon_code     = models.CharField(max_length=50, blank=True)
    payment_status  = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    order_status    = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='placed')
    razorpay_order_id  = models.CharField(max_length=100, blank=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
    created_at      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"

    class Meta:
        ordering = ['-created_at']


class OrderItem(models.Model):
    order        = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product_id   = models.IntegerField()
    product_name = models.CharField(max_length=200)
    img_url      = models.URLField(max_length=500, blank=True)
    price        = models.DecimalField(max_digits=10, decimal_places=2)
    quantity     = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.product_name} x{self.quantity}"

    @property
    def line_total(self):
        return self.price * self.quantity
