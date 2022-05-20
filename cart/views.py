from django.views.generic import TemplateView

from products.models import Category
from cart.models import Cart
from utils.utils import DataMixin


class CartPageView(DataMixin, TemplateView):
    template_name = 'cart/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_user_context(title='Корзина')
        return {**context, **data}


class ShippingPageView(DataMixin, TemplateView):
    template_name = 'cart/shipping.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_user_context(title='Оформление')
        return {**context, **data}


class ShippingAddressPageView(DataMixin, TemplateView):
    template_name = 'cart/shipping_address.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_user_context(title='Оформление')
        return {**context, **data}


class PaymentPageView(DataMixin, TemplateView):
    template_name = 'cart/payment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_user_context(title='Оформление')
        return {**context, **data}
