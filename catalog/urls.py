from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductDetailView, ProductListView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", ProductListView.as_view(), name="product_list"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="product_detail"),
    path('create/', ProductDetailView.as_view(), name="product_detail"),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name="product_detail"),
    path("contacts/", contacts, name="catalog"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
