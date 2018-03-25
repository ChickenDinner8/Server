from django.db import models


# Create your models here.
class Menu(models.Model):
    foodName = models.CharField(max_length=200)
    foodPrice = models.DecimalField(max_digits=4, decimal_places=1)


class Order(models.Model):
    payment = models.DecimalField(max_digits=4, decimal_places=1)
    # TODO: how to present food ordered by customer ?
