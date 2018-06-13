from django.http import HttpResponse
from ServerApp import models
from .auth_required_decorator import eatdd_login_required
from . import utils
from . import food_ctrl
from django.views.decorators.http import require_http_methods
import json


@require_http_methods(["GET", "POST"])
@eatdd_login_required
def manage_table_order(request, restaurantId, tableId):
    if request.method == "POST":
        # create new order
        received_data = json.loads(request.body.decode('utf-8'))
        foods = received_data['foods']
        # First get the menu of this restaurant
        menu_queryset = models.Food.objects.filter(restaurant_id=restaurantId)
        food_objs = []
        total_price = 0;
        for item in foods:
            food_queryset = menu_queryset.filter(pk=item['food_id'])
            if food_queryset.exists() is False:
                return HttpResponse('Food with id : %s not exist.' % (item['food_id']), status=500)
            else:
                food_objs.append({"food": food_queryset.first(), "num": item['num']})
                total_price = total_price + food_queryset.first().price
        # Good to make order
        order = models.Order(user_id=request.session[utils.BUYER_USERNAME],
                             restaurant_id=restaurantId,
                             table=tableId,
                             totalPrice=total_price)
        order.save()
        for item in food_objs:
            order_item = models.OrderItem(order=order, food=item['food'], num=item['num'])
            order_item.save()


        return_result = {}
        return_result['order_id'] = order.pk
        return_result['restaurant_id'] = restaurantId
        return_result['table_id'] = tableId
        return_result['customer_id'] = request.session[utils.BUYER_USERNAME]
        return_result['order_time'] = order.time.__str__()
        return_result['total_price'] = order.totalPrice
        return_result['detail'] = []
        for item in food_objs:
            return_result['detail'].append({"food":food_ctrl.food_to_dict(item['food']), "num":item["num"]})
        return utils.eatDDJsonResponse(return_result)

    return HttpResponse('OK', status=200)


@require_http_methods(["GET"])
@eatdd_login_required
def manage_restaurant_order(request, restaurantId):
    pass


def order_to_dict(order):
    order_item_queryset = models.OrderItem.objects.filter(order=order)
