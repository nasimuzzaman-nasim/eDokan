from django.urls import path
from product.api.views import product_detail_view, ProductView #product_view


urlpatterns = [
    path('<slug:slug>/', product_detail_view, name='customer-product-detail-view'),
    path('', ProductView.as_view(), name='customer-product-view'),
]
