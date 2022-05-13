from django.views.generic import TemplateView, ListView

from products.models import Category, Product


class HomePageView(ListView):
    model = Product
    template_name = 'information/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        context['categories'] = Category.objects.all()
        context['cart_range'] = range(1, 3)
        context['products'] = Product.objects.all()[:6]
        return context


class AboutPageView(TemplateView):
    template_name = 'information/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О нас'
        context['cart_range'] = range(1, 3)
        context['categories'] = Category.objects.all()
        return context


class ContactPageView(TemplateView):
    template_name = 'information/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        context['cart_range'] = range(1, 3)
        context['categories'] = Category.objects.all()
        return context


class PageDevelopmentView(TemplateView):
    template_name = 'information/page_development.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Страница в разработке'
        context['categories'] = Category.objects.all()
        return context
