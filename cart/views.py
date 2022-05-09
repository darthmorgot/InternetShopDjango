from django.views.generic import TemplateView

from products.models import Category

categories = Category.objects.all()


class CartPageView(TemplateView):
    template_name = 'cart/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Корзина'
        context['cart_range'] = range(1, 3)
        context['categories'] = categories
        return context


class ShippingPageView(TemplateView):
    template_name = 'cart/shipping.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Оформление'
        context['cart_range'] = range(1, 3)
        context['categories'] = categories
        return context


class ShippingAddressPageView(TemplateView):
    template_name = 'cart/shipping_address.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Оформление'
        context['cart_range'] = range(1, 3)
        context['categories'] = categories
        return context


class PaymentPageView(TemplateView):
    template_name = 'cart/payment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Оформление'
        context['cart_range'] = range(1, 3)
        context['categories'] = categories
        return context
