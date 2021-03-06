from django.urls import path

from . import views
from . import boss_user_login_ctrl
from . import boss_user_ctrl
from . import food_ctrl
from . import restaurant_ctrl
from . import wechat_login_ctrl
from . import order_ctrl
from . import image_ctrl

urlpatterns = [
    path('boss/session', boss_user_login_ctrl.login, name='api_session'),
    path('boss/user', boss_user_ctrl.bossUserAdmin, name='api_bossUserAdmin'),
    path('restaurants', restaurant_ctrl.get_all_restaurant, name='api_restaurant'),
    path('restaurant', restaurant_ctrl.create_restaurant, name='create_restaurant'),
    path('restaurant/<int:restaurantId>/', restaurant_ctrl.manage_restaurant, name='manage_restaurant'),
    path('food/<int:restaurantId>', food_ctrl.create_food, name='create_food'),
    path('food/<int:restaurantId>/<int:foodId>', food_ctrl.manage_food, name='manage_food'),
    path('menu/<int:restaurantId>', food_ctrl.get_menu, name='get_menu'),
    path('buyer/session', wechat_login_ctrl.wechat_login, name='wechat_login'),
    path('restaurant/orders/<int:restaurantId>/<int:tableId>', order_ctrl.manage_table_order),
    path('restaurant/orders/<int:restaurantId>', order_ctrl.manage_restaurant_order),
    path('upload_image', image_ctrl.upload_image, name='upload_image'),
]
