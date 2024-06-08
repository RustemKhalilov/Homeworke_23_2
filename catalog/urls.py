from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="catalog_list"),
    path('product/<int:pk>/', product_detail, name="product_detail"),
    path("contacts/", contacts, name="catalog"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
