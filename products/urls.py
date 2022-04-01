from django.urls import path

from .views import HomePageView, PopupPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('popup/', PopupPageView.as_view(), name='popup'),
]
