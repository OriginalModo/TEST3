from django.db import models


class Order(models.Model):
    person_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='In progress')

class Product(models.Model):
    name = models.CharField(max_length=255)
    time_to_cook = models.PositiveIntegerField()

