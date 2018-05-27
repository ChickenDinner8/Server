from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('restaurant', views.boss, name='bossHomepage'),
    path('customer', views.customer, name='customerHomepage'),
]
