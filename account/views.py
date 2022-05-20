from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from account.forms import UserLoginForm
from utils.utils import DataMixin


class DashboardPageView(DataMixin, TemplateView):
    template_name = 'account/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_user_context(title='Личный кабинет')
        return {**context, **data}


class ForgotPasswordPageView(DataMixin, TemplateView):
    template_name = 'account/forgot_password.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_user_context(title='Сброс пароля')
        return {**context, **data}


class LoginPageView(DataMixin, LoginView):
    form_class = UserLoginForm
    template_name = 'account/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_user_context(title='Вход')
        return {**context, **data}

    def get_success_url(self):
        return reverse_lazy('home')


class AccountPageView(DataMixin, TemplateView):
    template_name = 'account/account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_user_context(title='Учетная запись')
        return {**context, **data}
