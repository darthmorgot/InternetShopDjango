from django.urls import path

from .views import CartPageView, ShippingPageView, PaymentPageView, ShippingAddressPageView

urlpatterns = [
    path('cart/', CartPageView.as_view(), name='cart'),
    path('shipping/', ShippingPageView.as_view(), name='shipping'),
    path('shipping-address/', ShippingAddressPageView.as_view(), name='shipping_address'),
    path('payment/', PaymentPageView.as_view(), name='payment'),
]
