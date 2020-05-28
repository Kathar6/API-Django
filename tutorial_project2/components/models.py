from django.db import models


class ComponentCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='')

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Component(models.Model):
    category = models.ForeignKey(ComponentCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(default='')
    price = models.FloatField(default=0)
    stock = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Component"
        verbose_name_plural = "Components"

    def __str__(self):
        return self.name
