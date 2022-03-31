from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    context = {
        'title': 'ВелоСам',
    }
    return render(request, 'products/index.html', context=context)


class HomePageView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ВелоСам'
        context['product_range'] = range(1, 7)
        context['cart_range'] = range(1, 3)
        return context
