from django.urls import path

from . import views

urlpatterns = [
    path('boss/login', views.login, name='login'),
    path('boss/user', views.bossUserAdmin, name='bossUserAdmin'),
    path('restaurants', views.req_restaurant, name='api_restaurant'),
    path('restaurant_page', views.boss, name='bossHomepage'),
    path('customer', views.customer, name='customerHomepage'),
]
