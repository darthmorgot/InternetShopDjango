from django.urls import path

from .views import DashboardPageView, AccountPageView, ForgotPasswordPageView, LoginPageView, UserRegistration, \
    UserLogout, login_register_user

urlpatterns = [
    path('dashboard/', DashboardPageView.as_view(), name='dashboard'),
    path('account/', AccountPageView.as_view(), name='account'),
    path('forgot-password/', ForgotPasswordPageView.as_view(), name='forgot_password'),
    path('login/', LoginPageView.as_view(), name='login_form'),
    path('register/', UserRegistration.as_view(), name='register_form'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('login_register/', login_register_user, name='login_register'),
]

