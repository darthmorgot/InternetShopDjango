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


class CategoryPageView(DataMixin, ListView):
    model = Product
    template_name = 'products/catalog.html'
    paginate_by = 4

    def get_category(self):
        return Category.objects.get(slug=self.kwargs['category_slug'])

    def get_queryset(self):
        category = self.get_category()
        if category.parent:
            products = Product.objects.filter(category__slug=self.kwargs['category_slug']).select_related('category')
        else:
            products = Product.objects.filter(category__parent_id=category.pk).select_related('category')
        return products

    def get_context_data(self, **kwargs):
        category = self.get_category()
        context = super().get_context_data(**kwargs)
        if category.parent:
            context['number_products'] = \
                Product.objects.filter(category_id=category.pk).select_related('category').count()
            data = self.get_user_context(title=category.parent.name + ' ' + category.name)
        else:
            context['number_products'] = \
                Product.objects.filter(category__parent_id=category.pk).select_related('category').count()
            data = self.get_user_context(title=category.name)
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
