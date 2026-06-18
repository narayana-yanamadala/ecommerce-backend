from rest_framework import generics, permissions, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


# ── Public endpoints ──────────────────────────────────────

class ProductListView(generics.ListAPIView):
    """GET /api/store/products/ — list all products (public)"""
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['productName', 'category__slug']
    ordering_fields = ['price', 'avgRating', 'created_at']

    def get_queryset(self):
        qs = Product.objects.filter(inStock=True)
        category = self.request.query_params.get('category')
        if category:
            qs = qs.filter(category__slug=category)
        return qs


class ProductDetailView(generics.RetrieveAPIView):
    """GET /api/store/products/<id>/ — single product (public)"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class CategoryListView(generics.ListAPIView):
    """GET /api/store/categories/ — list all categories (public)"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


# ── Admin-only CRUD endpoints ─────────────────────────────

class ProductCreateView(generics.CreateAPIView):
    """POST /api/store/products/add/ — add product (admin only)"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]


class ProductUpdateView(generics.RetrieveUpdateDestroyAPIView):
    """PUT/PATCH/DELETE /api/store/products/<id>/manage/ — manage product (admin only)"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]


class CategoryCreateView(generics.ListCreateAPIView):
    """POST /api/store/categories/add/ — add category (admin only)"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]


@api_view(['POST'])
@permission_classes([IsAdminUser])
def bulk_add_products(request):
    """POST /api/store/products/bulk/ — add multiple products at once"""
    if not isinstance(request.data, list):
        return Response({'error': 'Send a JSON array of products.'}, status=400)

    created = []
    errors = []
    for item in request.data:
        serializer = ProductSerializer(data=item)
        if serializer.is_valid():
            serializer.save()
            created.append(serializer.data['productName'])
        else:
            errors.append({'item': item.get('productName', '?'), 'errors': serializer.errors})

    return Response({
        'created': created,
        'created_count': len(created),
        'errors': errors,
    })
