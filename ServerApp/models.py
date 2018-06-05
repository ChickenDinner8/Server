from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class BusinessUser(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    password = models.TextField()
    avatar = models.URLField()


class NormalUser(models.Model):
    open_id = models.CharField(max_length=100)
    avatar = models.URLField()


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()
    description = models.CharField(max_length=100)
    boss = models.ForeignKey(BusinessUser, on_delete=models.CASCADE)


class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=5, max_digits=10)
    description = models.TextField()
    image = models.URLField()
    priority = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class Order(models.Model):
    userId = models.ForeignKey(NormalUser, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    time = models.TimeField(auto_now=True)
    totalPrice = models.DecimalField(decimal_places=5, max_digits=10)


class OrderItem(models.Model):
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE)
    foodId = models.ForeignKey(Food, on_delete=models.CASCADE)
    num = models.IntegerField()
