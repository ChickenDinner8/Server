from django.urls import path

from . import views

urlpatterns = [
    path('boss/login', views.login, name='login'),
    path('boss/user', views.bossUserAdmin, name='bossUserAdmin'),
    path('restaurant', views.boss, name='bossHomepage'),
    path('customer', views.customer, name='customerHomepage'),
]
