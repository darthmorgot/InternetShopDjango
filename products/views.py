from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    context = {
        'title': 'ВелоСам',
    }
    return render(request, 'products/index.html', context=context)


class HomeView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ВелоСам'
        return context
