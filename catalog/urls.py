from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductDetailView, ProductListView, ProductUpdateView, ProductCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", ProductListView.as_view(), name="list"),
    path('create/', ProductCreateView.as_view(), name="create"),
    path('view/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name="view"),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name="edit"),
    path("contacts/", contacts, name="contact"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
