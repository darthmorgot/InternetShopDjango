from django.urls import path

from .views import ProductQuickViewView, CatalogPageView, ProductPageView, test

urlpatterns = [
    path('quick-view/', ProductQuickViewView.as_view(), name='quick_view'),
    path('product/', ProductPageView.as_view(), name='product'),
    path('catalog/', CatalogPageView.as_view(), name='catalog'),
    path('catalog/<slug:category_slug>', test, name='product_by_category'),
]
