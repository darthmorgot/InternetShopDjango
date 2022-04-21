from django.urls import path

from .views import ProductQuickViewView, CatalogPageView, ProductPageView

urlpatterns = [
    path('quick-view/', ProductQuickViewView.as_view(), name='quick_view'),
    path('product/', ProductPageView.as_view(), name='product'),
    path('catalog/', CatalogPageView.as_view(), name='catalog'),
]

