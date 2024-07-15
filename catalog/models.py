from django.db import models
from users.models import User
from config.settings import NULLABLE


# Create your models here.
class Category(models.Model):
    # Описание поля наименование
    name = models.CharField(
        max_length=100,
        verbose_name="Категория",
        help_text="Введите название категории")
    # Описание поля описание
    description = models.TextField(
        verbose_name="Название категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Название категории"
        verbose_name_plural = "Категории"

    #     ordering = ["breed", "name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    # Описание поля наименование
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Наименование продукта",
    )
    # Описание поля описаение
    description = models.TextField(
        verbose_name="Название продукта",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
    )
    # Описание поля категория
    my_category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория продукта",
        help_text="Введите название категории",
        null=True,
        blank=True,
        related_name="category_product",
    )

    # Описание поля изображение
    foto = models.ImageField(
        upload_to="catalog/photo",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите фото товара",
    )
    # Описание поля наименование
    price = models.CharField(
        max_length=100,
        verbose_name="Цена за единицу",
        help_text="Укажите цену за единицу",
    )
    # Описание поля дата создания записи
    created_at = models.DateTimeField(
        blank=True,
        verbose_name="Дата записи в БД",
        help_text="Укажите дату создания записи БД",
    )

    owner = models.ForeignKey(
        User,
        verbose_name='Владелец',
        help_text='Укажите владельца',
        on_delete=models.SET_NULL,
        **NULLABLE
    )

    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликован"
    )


    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        permissions = [
                       ("can_edit_publication", "Can_edit_publication"),
                       ("can_edit_dicription", "Can_edit_dicription"),
                       ("can_edit_category", "Can_edit_category")
                       ]

    def __str__(self):
        return self.name


class Version(models.Model):
    name = models.ForeignKey(Product, verbose_name='продукт', on_delete=models.CASCADE, related_name='versions')
    version_number = models.PositiveIntegerField(verbose_name='Номер версии')
    version_name = models.CharField(max_length=100, verbose_name="Название версии")
    version_now = models.BooleanField(
        default=True, verbose_name="Признак текущей версии"
    )

    def __str__(self):
        # Строковое отображение объекта
        return f"{self.version_name} | {self.version_number}"

    class Meta:
        verbose_name = "Версия"  # Настройка для наименования одного объекта
        verbose_name_plural = "Версии"  # Настройка для наименования набора объектов
