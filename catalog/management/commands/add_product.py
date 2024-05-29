from django.core.management import BaseCommand
from catalog.models import Category, Product
import json

class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('products_info.json', encoding='utf-8') as json_file:
            return json.load(json_file)
        # Здесь мы получаем данные из фикстур с категориями

    @staticmethod
    def json_read_products():
        with open('products_info.json', encoding='utf-8') as json_file:
             return json.load(json_file)



    def handle(self, *args, **options):

        # Удалите все продукты
        Product.objects.all().delete()

        # Удалите все категории
        Category.objects.all().delete()


        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for item in Command.json_read_categories():
            if item["model"] == "catalog.category":
                category_for_create.append(
                    {"id": item['pk'],
                     "name": item['fields']['name'],
                     "description": item['fields']['description']}
                )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        #Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for item in Command.json_read_products():
            if item["model"] == "catalog.product":
                product_for_create.append(
                    {"id": item['pk'],
                     "name": item['fields']['name'],
                     "description": item['fields']['description'],
                     "my_category": item['fields']['my_category'],
                     "foto": item['fields']['foto'],
                     "created_at": item['fields']['created_at'],
                     "updated_at": item['fields']['updated_at'],
                     "manufactured_at": item['fields']['manufactured_at'],
                     }
                   )
       # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)


