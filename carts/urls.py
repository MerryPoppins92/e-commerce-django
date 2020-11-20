from django.urls import path

from carts.views import (
    cart_update, 
    checkout_home,
    cart_home, 
    checkout_done_view,
    )

app_name = 'instance'

urlpatterns = [
    path('', cart_home, name='home'),
    path('checkout/', checkout_home, name='checkout'),
    path('checkout/success/', checkout_done_view, name='success'),
    path('update/', cart_update, name='update'),
]