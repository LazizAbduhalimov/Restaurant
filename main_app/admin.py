from django.contrib import admin
from main_app.models import *


@admin.register(Slider)
class AdminSlider(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
        "admin_image",
        "is_active",
    ]
    list_per_page = 15


@admin.register(Feature)
class AdminFeature(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
        "admin_image",
        "is_active",
    ]
    list_per_page = 15


@admin.register(Chef)
class AdminChef(admin.ModelAdmin):
    list_display = [
        "name",
        "about",
        "social_net",
        "admin_image",
        "is_active",
    ]
    list_per_page = 15


@admin.register(News)
class AdminNews(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
        "published_data",
        "admin_image",
        "is_active",
    ]
    list_per_page = 15


@admin.register(GalleryFood)
class AdminGalleryFood(admin.ModelAdmin):
    list_display = [
        "admin_image",
        "is_active",
    ]
    list_editable = ["is_active"]
    list_per_page = 15


@admin.register(GalleryRestaurant)
class AdminNews(admin.ModelAdmin):
    list_display = [
        "admin_image",
        "is_active",
    ]
    list_editable = ["is_active"]
    list_per_page = 15


@admin.register(OrderProducts)
class AdminOrder(admin.ModelAdmin):
    list_display = [
        "user_id",
        "order",
        "phone",
        "location",
        "order_date",
        "order_accept",
        "is_delivered",
    ]
    list_per_page = 15


@admin.register(Client)
class AdminClient(admin.ModelAdmin):
    list_display = [
        "person_id",
        "tel",
        "comment",
    ]
    list_per_page = 15


@admin.register(Products)
class AdminProducts(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "category",
        "price",
        "size",
        "is_active",
        "admin_image",
    ]
    readonly_fields = ["category_slug"]
    list_per_page = 15


@admin.register(ProductsCategory)
class AdminProductsCategory(admin.ModelAdmin):
    list_display = [
        "name",
        "is_active",
    ]
    list_per_page = 15
