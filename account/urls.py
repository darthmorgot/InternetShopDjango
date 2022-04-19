from django.urls import path

from .views import DashboardPageView, ForgotPasswordPageView, LoginPageView, AccountPageView

urlpatterns = [
    path('dashboard/', DashboardPageView.as_view(), name='dashboard'),
    path('forgot-password/', ForgotPasswordPageView.as_view(), name='forgot_password'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('account/', AccountPageView.as_view(), name='account'),
]
