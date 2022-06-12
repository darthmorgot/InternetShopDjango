from django.urls import path

from .views import ProductQuickViewView, CatalogPageView, ProductPageView, CategoryPageView

urlpatterns = [
    path('quick-view/<int:pk>', ProductQuickViewView.as_view(), name='quick_view'),
    path('product/<int:product_id>', ProductPageView.as_view(), name='product'),
    path('catalog/<slug:category_slug>', CategoryPageView.as_view(), name='product_by_category'),
    path('catalog/', CatalogPageView.as_view(), name='catalog'),
]
