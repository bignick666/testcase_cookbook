from django.shortcuts import render
from .models import Dish, Product, Recipe


def show_recipe_without_product(request, product_id):
    product = Product.objects.get(id=product_id)
    recipes = Recipe.objects.exclude(product__id=product_id)

    return render(request, 'index.html', {'recipes': recipes, 'product': product})
