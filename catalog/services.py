from catalog.models import Product, Category
from config.settings import CACHE_ENABLE
from django.core.cache import cache


def get_product_from_cache():
    """
    Получает данные по продуктам из кеша если она там есть или из базы данных
    """
    if not CACHE_ENABLE:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


def get_category_from_cache():
    """
    Получает данные по категориям из кэша,
    если кеш пуст, получает данные из бд.
    """
    if not CACHE_ENABLE:
        return Category.objects.all()
    key = "category_list"
    category = cache.get(key)
    if category is not None:
        return category
    category = Category.objects.all()
    cache.set(key, category)
    return category
