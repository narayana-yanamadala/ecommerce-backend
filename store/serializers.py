from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.slug', read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Product
        fields = [
            'id', 'productName', 'category', 'category_id',
            'price', 'imgUrl', 'shortDesc', 'description',
            'avgRating', 'inStock', 'discount', 'created_at'
        ]
