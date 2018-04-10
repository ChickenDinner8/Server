from django.urls import path

from . import views

urlpatterns = [
    path('restaurant', views.boss, name='bossHomepage'),
    path('customer', views.customer, name='customerHomepage'),
]
