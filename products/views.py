from django.views.generic import TemplateView


class ProductQuickViewView(TemplateView):
    template_name = 'products/popup/product_quick_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CatalogPageView(TemplateView):
    template_name = 'products/catalog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Каталог'
        context['product_range'] = range(1, 11)
        context['cart_range'] = range(1, 3)
        return context


class ProductPageView(TemplateView):
    template_name = 'products/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Товар'
        context['product_range'] = range(1, 7)
        context['cart_range'] = range(1, 3)
        return context
