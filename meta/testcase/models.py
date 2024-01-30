from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название продукта')
    count = models.IntegerField(verbose_name='Количество использований в блюдах', default=0)

    def __str__(self):
        return f'{self.name}'


class Dish(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название блюда')
    products = models.ManyToManyField(Product, through='Recipe', related_name='products')

    def __str__(self):
        return self.name


class Recipe(models.Model):
    product = models.ForeignKey(Product, related_name='recipes', on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, related_name='recipes', on_delete=models.CASCADE)
    weight = models.IntegerField(verbose_name='граммовка')

    class Meta:
        unique_together = ('product', 'dish')


@receiver(post_save, sender=Recipe)
def count_changed(instance, **kwargs):
    rs = instance.product
    rs.count += 1
    rs.save()
