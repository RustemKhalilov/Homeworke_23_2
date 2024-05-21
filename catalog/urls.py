from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='catalog'),
    path('contacts/', contacts, name='catalog')
]
