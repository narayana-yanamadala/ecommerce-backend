from django.urls import path
from . import views

urlpatterns = [
    # Public
    path('products/',              views.ProductListView.as_view(),    name='product-list'),
    path('products/<int:pk>/',     views.ProductDetailView.as_view(),  name='product-detail'),
    path('categories/',            views.CategoryListView.as_view(),   name='category-list'),

    # Admin only
    path('products/add/',          views.ProductCreateView.as_view(),  name='product-add'),
    path('products/<int:pk>/manage/', views.ProductUpdateView.as_view(), name='product-manage'),
    path('products/bulk/',         views.bulk_add_products,            name='product-bulk'),
    path('categories/add/',        views.CategoryCreateView.as_view(), name='category-add'),
]
