from django.contrib import admin
from .models import Address, Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'user', 'city', 'state', 'pincode', 'address_type', 'is_default']
    list_filter  = ['address_type', 'is_default', 'state']
    search_fields = ['full_name', 'phone', 'city']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_amount', 'payment_method', 'payment_status', 'order_status', 'created_at']
    list_filter  = ['payment_method', 'payment_status', 'order_status']
    inlines      = [OrderItemInline]
    readonly_fields = ['created_at']
