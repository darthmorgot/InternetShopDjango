from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from account.forms import UserLoginForm, UserRegistrationForm, UserPasswordResetForm, UserPasswordResetConfirmForm
from utils.utils import DataMixin, get_context


class DashboardPageView(DataMixin, TemplateView):
    template_name = 'account/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_user_context(title='Личный кабинет')
        return {**context, **data}


class AccountPageView(DataMixin, TemplateView):
    template_name = 'account/account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_user_context(title='Учетная запись')
        return {**context, **data}


class PasswordResetPageView(DataMixin, PasswordResetView):
    form_class = UserPasswordResetForm
    template_name = 'account/password_reset_form.html'
    subject_template_name = 'account/password_reset_subject.txt'
    email_template_name = 'account/password_reset_email.txt'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_user_context(title='Сброс пароля')
        return {**context, **data}


class PasswordResetDonePageView(DataMixin, PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_user_context(title='Письмо на сброс пароля')
        return {**context, **data}


class PasswordResetConfirmPageView(DataMixin, PasswordResetConfirmView):
    form_class = UserPasswordResetConfirmForm
    template_name = 'account/password_reset_confirm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_user_context(title='Изменить пароль')
        if self.validlink:
            context['validlink'] = True
        else:
            context.update({'form': None, 'validlink': False})
        return {**context, **data}


class PasswordResetCompletePageView(DataMixin, PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_user_context(title='Пароль успешно изменен')
        return {**context, **data}


class UserRegistration(SuccessMessageMixin, DataMixin, CreateView):
    form_class = UserRegistrationForm
    template_name = 'account/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_user_context(title='Вход')
        return {**context, **data}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, 'Спасибо за регистрацию в интернет-магазине "ВелоСам"!')
        return redirect('dashboard')

    def form_invalid(self, form):
        messages.warning(self.request, 'Пользователь с таким email уже существует.')
        return redirect('login_register')


class LoginPageView(SuccessMessageMixin, DataMixin, LoginView):
    form_class = UserLoginForm
    template_name = 'account/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_user_context(title='Вход')
        return {**context, **data}

    def get_success_url(self):
        messages.info(self.request, ' ')
        return reverse_lazy('dashboard')

    def form_invalid(self, form):
        messages.error(self.request, 'Введеные email или пароль неверны.')
        return redirect('login_register')


class UserLogout(LogoutView):
    next_page = reverse_lazy('home')


def login_register_user(request):
    login_form = UserLoginForm()
    register_form = UserRegistrationForm()
    data = get_context(title='Вход-Регистрация')

    context = {
        'register_form': register_form,
        'login_form': login_form,
    }
    context = {**context, **data}
    return render(request, 'account/login.html', context=context)
