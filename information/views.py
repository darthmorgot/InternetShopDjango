from django.views.generic import TemplateView, ListView

from products.models import Category, Product
from utils.utils import DataMixin


class HomePageView(DataMixin, ListView):
    model = Product
    template_name = 'information/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()[:6]
        data = self.get_user_context(title='Главная')
        return {**context, **data}
        # context['title'] = 'Главная'
        # context['categories'] = Category.objects.all()
        # context['cart_range'] = range(1, 3)
        # return context


class AboutPageView(DataMixin, TemplateView):
    template_name = 'information/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_user_context(title='О нас')
        return {**context, **data}


class ContactPageView(DataMixin, TemplateView):
    template_name = 'information/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_user_context(title='Контакты')
        return {**context, **data}


class PageDevelopmentView(DataMixin, TemplateView):
    template_name = 'information/page_development.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_user_context(title='Страница в разработке')
        return {**context, **data}
