from django.contrib import admin
from .models import Product, Dish, Recipe


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'name', 'count']
    list_filter = ['name']


@admin.register(Dish)
class AdminDish(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']


@admin.register(Recipe)
class AdminRecipe(admin.ModelAdmin):
    list_display = ['id', 'product', 'dish', 'weight']
    list_filter = ['product', 'dish']
