from django.urls import path

from .views import AboutPageView, ContactPageView, PageDevelopmentView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('page-development/', PageDevelopmentView.as_view(), name='page_development'),
]
