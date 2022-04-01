from django.views.generic import TemplateView


class AboutPageView(TemplateView):
    template_name = 'information/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О нас'
        context['cart_range'] = range(1, 3)
        return context


class ContactPageView(TemplateView):
    template_name = 'information/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        context['cart_range'] = range(1, 3)
        return context
