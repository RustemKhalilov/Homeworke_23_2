from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from catalog.apps import CatalogConfig
from catalog.views import home, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('admin/', admin.site.urls),
#    path('', include('main.urls')),
    path('', home, name='catalog'),
    path('contacts/', contacts, name='catalog')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
