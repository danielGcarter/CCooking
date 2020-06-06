from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    background = models.CharField(max_length=150)
    process = models.TextField()
    categories = models.ManyToManyField('Category', related_name='recipes')


class Ingredient(models.Model):
    name = models.CharField(max_length=150)
    unit = models.CharField(max_length=150)
    amount = models.FloatField()
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=100)