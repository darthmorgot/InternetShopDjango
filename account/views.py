from django.views.generic import TemplateView


class DashboardPageView(TemplateView):
    template_name = 'account/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Личный кабинет'
        context['cart_range'] = range(1, 3)
        return context
