from django.db import models


# категории товаров
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Категория")
    slug = models.SlugField(unique=True, verbose_name="Слаг")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


# товат
class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Наименование")
    slug = models.SlugField(unique=True, verbose_name="Слаг")
    image = models.ImageField(verbose_name="Изображение", upload_to="product/")    # TODO загружать несколько картинок к одному товару
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


# продуск для корзины
class CartProduct:
    pass


# корвзина
class Cart:
    pass


# заказ
class Order:
    pass
