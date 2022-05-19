from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from account.forms import UserLoginForm
from products.models import Category


class DashboardPageView(TemplateView):
    template_name = 'account/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Личный кабинет'
        context['cart_range'] = range(1, 3)
        context['categories'] = Category.objects.all()
        return context


class ForgotPasswordPageView(TemplateView):
    template_name = 'account/forgot_password.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Сброс пароля'
        context['cart_range'] = range(1, 3)
        context['categories'] = Category.objects.all()
        return context


class LoginPageView(LoginView):
    form_class = UserLoginForm
    template_name = 'account/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход'
        context['cart_range'] = range(1, 3)
        context['categories'] = Category.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('home')


class AccountPageView(TemplateView):
    template_name = 'account/account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Учетная запись'
        context['cart_range'] = range(1, 3)
        context['categories'] = Category.objects.all()
        return context
