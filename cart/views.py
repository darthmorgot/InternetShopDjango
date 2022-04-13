from django.views.generic import TemplateView


class CartPageView(TemplateView):
    template_name = 'cart/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Корзина'
        context['cart_range'] = range(1, 3)
        return context
