from django.db import models


# Create your models here.
class Menu(models.Model):
    foodName = models.CharField(max_length=200)
    foodPrice = models.DecimalField(max_digits=4, decimal_places=1)
    foodDescription = models.TextField()
    foodImage = models.ImageField()
    foodPriority = models.IntegerField()


class Order(models.Model):
    orderID = models.IntegerField(primary_key=True)
    orderTime = models.TimeField()
    tableNum = models.IntegerField()
    foodOfOrder = models.CharField(max_length=1024)  # maybe JSON is a good choice?
    payment = models.DecimalField(max_digits=4, decimal_places=1)
