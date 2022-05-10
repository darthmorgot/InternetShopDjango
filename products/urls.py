from django.urls import path

from .views import ProductQuickViewView, CatalogPageView, ProductPageView

urlpatterns = [
    path('quick-view/', ProductQuickViewView.as_view(), name='quick_view'),
    path('product/', ProductPageView.as_view(), name='product'),
    path('product/<int:product_id>', ProductPageView.as_view(), name='product_test'),
    path('catalog/', CatalogPageView.as_view(), name='catalog'),
    path('catalog/<slug:category_slug>', CatalogPageView.as_view(), name='product_by_category'),
]
