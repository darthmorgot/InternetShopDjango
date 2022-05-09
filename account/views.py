from django.views.generic import TemplateView

from products.models import Category

categories = Category.objects.all()


class DashboardPageView(TemplateView):
    template_name = 'account/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Личный кабинет'
        context['cart_range'] = range(1, 3)
        context['categories'] = categories
        return context


class ForgotPasswordPageView(TemplateView):
    template_name = 'account/forgot_password.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Сброс пароля'
        context['cart_range'] = range(1, 3)
        context['categories'] = categories
        return context


class LoginPageView(TemplateView):
    template_name = 'account/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход'
        context['cart_range'] = range(1, 3)
        context['categories'] = categories
        return context


class AccountPageView(TemplateView):
    template_name = 'account/account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Учетная запись'
        context['cart_range'] = range(1, 3)
        context['categories'] = categories
        return context
