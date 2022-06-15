from django.urls import path

from .views import \
    DashboardPageView, AccountPageView, LoginPageView, UserRegistration, UserLogout, login_register_user, \
    PasswordResetPageView, PasswordResetDonePageView, PasswordResetConfirmPageView, PasswordResetCompletePageView


urlpatterns = [
    path('dashboard/', DashboardPageView.as_view(), name='dashboard'),
    path('account/', AccountPageView.as_view(), name='account'),
    path('password_reset/', PasswordResetPageView.as_view(), name='password_reset_form'),
    path('password_reset_done/', PasswordResetDonePageView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', PasswordResetConfirmPageView.as_view(),
         name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompletePageView.as_view(), name='password_reset_complete'),
    path('login/', LoginPageView.as_view(), name='login_form'),
    path('register/', UserRegistration.as_view(), name='register_form'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('login_register/', login_register_user, name='login_register'),
]
