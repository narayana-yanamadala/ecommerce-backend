from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display  = ['productName', 'category', 'price', 'avgRating', 'inStock', 'discount', 'created_at']
    list_filter   = ['category', 'inStock']
    search_fields = ['productName']
    list_editable = ['price', 'inStock', 'discount']
    readonly_fields = ['created_at']

    fieldsets = (
        ('Basic Info', {
            'fields': ('productName', 'category', 'price', 'discount', 'inStock')
        }),
        ('Image', {
            'fields': ('imgUrl',),
            'description': 'Paste any public image URL — Unsplash, Amazon product image, etc.'
        }),
        ('Description', {
            'fields': ('shortDesc', 'description', 'avgRating')
        }),
        ('Meta', {
            'fields': ('created_at',)
        }),
    )
