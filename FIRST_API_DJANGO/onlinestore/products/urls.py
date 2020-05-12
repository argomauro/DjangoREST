from django.urls import path
from products.views import (ProductDetailView, ProductListView, 
                            product_list, 
                            product_detail, manufacturer_list, manufacturer_detail)

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='detail-list'),
    path('products-rest', product_list, name='product-list'),
    path('product-rest/<int:pk>/', product_detail, name='product-detail'),
    path('manufacturers-rest', manufacturer_list, name='manufacturer_list'),
    path('manufacturer-rest/<int:pk>/', manufacturer_detail, name='manufacturer_detail'),
]

