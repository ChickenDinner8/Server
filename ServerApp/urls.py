from django.urls import path

from . import views
from . import boss_user_login_ctrl
from . import boss_user_ctrl
from . import food_ctrl
from . import restaurant_ctrl

urlpatterns = [
    path('boss/login', boss_user_login_ctrl.login, name='api_login'),
    path('boss/user', boss_user_ctrl.bossUserAdmin, name='api_bossUserAdmin'),
    path('restaurants', restaurant_ctrl.get_all_restaurant, name='api_restaurant'),
    path('restaurant_page', views.boss, name='bossHomepage'),
    path('customer', views.customer, name='customerHomepage'),
]
