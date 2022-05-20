from django.views.generic import DetailView, ListView

from products.models import Category, Product, Image
from utils.utils import DataMixin


class ProductQuickViewView(DetailView):
    model = Product
    template_name = 'products/popup/product_quick_view.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Image.objects.filter(product__pk=self.kwargs['pk'])
        return context


class CatalogPageView(DataMixin, ListView):
    model = Product
    template_name = 'products/catalog.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        products = Product.objects.all()
        context = super().get_context_data(**kwargs)
        context['products'] = products
        context['number_products'] = products.count()
        data = self.get_user_context(title='Каталог')
        return {**context, **data}


class ProductPageView(DataMixin, DetailView):
    model = Product
    template_name = 'products/product.html'
    pk_url_kwarg = 'product_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(pk=self.kwargs['product_id'])
        context['products'] = Product.objects.all()[:6]
        context['images'] = Image.objects.filter(product__pk=self.kwargs['product_id'])
        data = self.get_user_context(title='Товар')
        return {**context, **data}
