from django.contrib import admin

from .models import *


@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    pass


@admin.register(Tag)
class AdminTag(admin.ModelAdmin):
    pass


@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'published_date',
        'is_active',
        'admin_image',
    ]


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = [
        'user',
        'is_author',
        'get_staff_status',
        'get_active_status',
        'admin_image',
    ]


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    pass