from django.urls import path

from products.views import (
    # product_list_view, 
    ProductListView, 
    # ProductDetailView,
    ProductDetailSlugView, 
    # product_detail_view,
    # ProductFeaturedListView,
    # ProductFeaturedDetailView
    )

app_name = 'instance'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<slug:slug>/', ProductDetailSlugView.as_view(), name='detail'),
]