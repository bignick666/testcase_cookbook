from django.urls import path, include

from . import views

app_name = 'testcase'

urlpatterns = [
    path('<int:product_id>', views.show_recipe_without_product)
]
