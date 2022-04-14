from django.urls import path

from .views import CartPageView, ShippingPageView

urlpatterns = [
    path('cart/', CartPageView.as_view(), name='cart'),
    path('shipping/', ShippingPageView.as_view(), name='shipping'),
]
