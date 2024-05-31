from django.db import models


# Create your models here.
class Category(models.Model):
    # Описание поля наименование
    name = models.CharField(
        max_length=100,
        verbose_name="Категория",
        help_text="Введите название категории")
    # Описание поля описаение
    description = models.TextField(
        verbose_name="Название категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    # имя, порода, фото, дата рождения
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
    # Описание поля дата изменения записи в БД
    updated_at = models.DateTimeField(
        blank=True,
        verbose_name="Дата записи в БД",
        help_text="Укажите изменения записи в БД",
    )

    # Описание поля дата изменения дата производства
    manufactured_at = models.DateTimeField(
        blank=True,
        verbose_name="Дата производства",
        help_text="Укажите дату производства",
    )

    # имя, порода, фото, дата рождения
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name
