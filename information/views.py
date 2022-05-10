from django.views.generic import TemplateView, ListView

from products.models import Category, Product

categories = Category.objects.all()


class HomePageView(ListView):
    model = Product
    template_name = 'information/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        context['categories'] = categories
        context['product_range'] = range(1, 7)
        context['cart_range'] = range(1, 3)
        context['products'] = Product.objects.all()[:6]
        return context


class AboutPageView(TemplateView):
    template_name = 'information/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О нас'
        context['cart_range'] = range(1, 3)
        context['categories'] = categories
        return context


class ContactPageView(TemplateView):
    template_name = 'information/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        context['cart_range'] = range(1, 3)
        context['categories'] = categories
        return context


class PageDevelopmentView(TemplateView):
    template_name = 'information/page_development.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Страница в разработке'
        context['categories'] = categories
        return context
