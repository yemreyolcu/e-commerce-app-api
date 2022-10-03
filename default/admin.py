from django.contrib import admin
from .models import Brand, OS


# Register your models here.


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(OS)
class OSAdmin(admin.ModelAdmin):
    list_display = ['name']
