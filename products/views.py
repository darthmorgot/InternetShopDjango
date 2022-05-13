from django.views.generic import DetailView, ListView

from products.models import Category, Product, Image


class ProductQuickViewView(DetailView):
    model = Product
    template_name = 'products/popup/product_quick_view.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Image.objects.filter(product__pk=self.kwargs['pk'])
        return context


class CatalogPageView(ListView):
    model = Product
    template_name = 'products/catalog.html'

    def get_context_data(self, **kwargs):
        products = Product.objects.all()
        context = super().get_context_data(**kwargs)
        context['title'] = 'Каталог'
        context['cart_range'] = range(1, 3)
        context['categories'] = Category.objects.all()
        context['products'] = products
        context['number_products'] = products.count()
        return context


class ProductPageView(DetailView):
    model = Product
    template_name = 'products/product.html'
    pk_url_kwarg = 'product_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Товар'
        context['cart_range'] = range(1, 3)
        context['categories'] = Category.objects.all()
        context['product'] = Product.objects.get(pk=self.kwargs['product_id'])
        context['products'] = Product.objects.all()[:6]
        context['images'] = Image.objects.filter(product__pk=self.kwargs['product_id'])
        return context
