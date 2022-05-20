from products.models import Category


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['cart_range'] = range(1, 3)
        context['categories'] = Category.objects.all()
        return context
