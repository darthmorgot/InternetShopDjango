from django.urls import path

from .views import HomePageView, ProductQuickViewView, CatalogPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('quick-view/', ProductQuickViewView.as_view(), name='quick_view'),
    path('catalog/', CatalogPageView.as_view(), name='catalog'),
]
