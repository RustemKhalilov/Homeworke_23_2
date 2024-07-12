from django.contrib import admin
from catalog.models import Product
from catalog.models import Category
from catalog.models import Version

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "my_category")
    list_filter = ("my_category",)
    search_fields = ("description",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ("name", "version_number", "version_name", "version_now")


