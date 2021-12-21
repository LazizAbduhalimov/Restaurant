from django.db import models
from ckeditor.fields import RichTextField


class Slider(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=30)
    description = models.CharField(verbose_name="Подзаголовок", max_length=150)
    image = models.ImageField(verbose_name="Фото", default="/static/PhotoNotFound", upload_to="images/sliders/")
    is_active = models.BooleanField(verbose_name="Активность", default=False)

    def admin_image(self):

        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(
                f'<a href="{self.image.url}" target="_blank"><img src="{self.image.url}" width="180" /></a>'
            )
        else:
            return 'Not Image Found'

    admin_image.short_description = 'Photo'
    admin_image.allow_tags = True

    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайдеры главного меню"


class Feature(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=40)
    description = models.CharField(verbose_name="Подзаголовок", max_length=200)
    image = models.ImageField(verbose_name="Фото", default="/static/PhotoNotFound", upload_to="images/features/")
    is_active = models.BooleanField(verbose_name="Активность", default=False)

    def admin_image(self):

        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(
                f'<a href="{self.image.url}" target="_blank"><img src="{self.image.url}" width="100" /></a>'
            )
        else:
            return 'Not Image Found'

    admin_image.short_description = 'Photo'
    admin_image.allow_tags = True

    class Meta:
        verbose_name = "Отличие"
        verbose_name_plural = "Отличия"


class Chef(models.Model):
    name = models.CharField(verbose_name="Имя шефа", max_length=30)
    about = models.CharField(verbose_name="О шефе", max_length=150)
    social_net = models.CharField(verbose_name="Ссылка на соц сеть", max_length=200)
    image = models.ImageField(verbose_name="Фото", default="/static/PhotoNotFound", upload_to="images/chefs/")
    is_active = models.BooleanField("Активность", default=False)

    def admin_image(self):

        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(
                f'<a href="{self.image.url}" target="_blank"><img src="{self.image.url}" width="100" /></a>'
            )
        else:
            return 'Not Image Found'

    admin_image.short_description = 'Photo'
    admin_image.allow_tags = True

    class Meta:
        verbose_name = "Шеф"
        verbose_name_plural = "Шефы"


class News(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=40)
    description = RichTextField(verbose_name="Содержание")
    image = models.ImageField(verbose_name="Фото", default="/static/PhotoNotFound", upload_to="images/news/")
    published_data = models.DateField(verbose_name="Дата публикации", auto_now=True)
    is_active = models.BooleanField(verbose_name="Активность", default=False)

    def admin_image(self):

        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(
                f'<a href="{self.image.url}" target="_blank"><img src="{self.image.url}" width="100" /></a>'
            )
        else:
            return 'Not Image Found'

    admin_image.short_description = 'Photo'
    admin_image.allow_tags = True

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class GalleryFood(models.Model):
    image = models.ImageField(verbose_name="Фото", default="/static/PhotoNotFound", upload_to="images/gallery/foods/")
    is_active = models.BooleanField(verbose_name="Активность", default=False)

    def admin_image(self):

        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(
                f'<a href="{self.image.url}" target="_blank"><img src="{self.image.url}" width="100" /></a>'
            )
        else:
            return 'Not Image Found'

    admin_image.short_description = 'Photo'
    admin_image.allow_tags = True

    class Meta:
        verbose_name = "Фото к галлерее"
        verbose_name_plural = "Фотографии продуктов галлереи"


class GalleryRestaurant(models.Model):
    image = models.ImageField(
        verbose_name="Фото", default="/static/PhotoNotFound", upload_to="images/gallery/restaurant"
    )
    is_active = models.BooleanField(verbose_name="Активность", default=False)

    def admin_image(self):

        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(
                f'<a href="{self.image.url}" target="_blank"><img src="{self.image.url}" width="100" /></a>'
            )
        else:
            return 'Not Image Found'

    admin_image.short_description = 'Photo'
    admin_image.allow_tags = True

    class Meta:
        verbose_name = "Фото к галлерее"
        verbose_name_plural = "Фотографии ресторана в галлерее"


class OrderProducts(models.Model):
    user_id = models.PositiveIntegerField("ID Клиента")
    order = models.TextField("Продукты заказа")
    phone = models.CharField("Номер телефона", max_length=100)
    location = models.CharField("Локатион", max_length=200)
    order_date = models.DateTimeField("Дата заказа", auto_now=True, editable=True)
    order_accept = models.DateTimeField("Дата заказа", auto_now_add=True, editable=True)
    is_delivered = models.BooleanField("Принят или нет", default=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"{self.user_id}"


class Client(models.Model):
    """информация о клиенте"""

    person_id = models.PositiveIntegerField("id телеграма")
    tel = models.CharField("Phone", max_length=20, blank=True)
    comment = models.TextField("Comment for client", blank=True)

    class Meta:
        verbose_name = 'Инфа о клиенте'
        verbose_name_plural = 'Инфа о клиентах'

    def __str__(self):
        return f'Клиент {self.person_id}'


class ProductsCategory(models.Model):
    name = models.CharField(verbose_name="Категория продуктов", max_length=30)
    is_active = models.BooleanField(verbose_name="Активность", default=False)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории продуктов"

    def __str__(self):
        return f"{self.name}"


class Products(models.Model):
    name = models.CharField(verbose_name="Название", max_length=20)
    description = RichTextField(verbose_name="Описание")
    image = models.ImageField(verbose_name="Фото", default="/static/PhotoNotFound", upload_to="images/products/")
    category = models.ForeignKey(ProductsCategory, verbose_name="Катеория", null=True, on_delete=models.SET_NULL)
    category_slug = models.CharField(max_length=30, blank=True)
    price = models.PositiveIntegerField(verbose_name="Цена", default=0)
    size = models.CharField(verbose_name="Размер", max_length=30)
    is_active = models.BooleanField(verbose_name="Активность", default=False)

    def save(self, *args, **kwargs):
        self.category_slug = self.category.name
        super(Products, self).save(*args, **kwargs)

    def admin_image(self):

        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(
                f'<a href="{self.image.url}" target="_blank"><img src="{self.image.url}" width="100" /></a>'
            )
        else:
            return 'Not Image Found'

    admin_image.short_description = 'Photo'
    admin_image.allow_tags = True

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"
