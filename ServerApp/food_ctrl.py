from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import json
from ServerApp import models
from .auth_required_decorator import eatdd_login_required
from . import utils

@require_http_methods(["GET", "PUT", "DELETE"])
@eatdd_login_required
def manage_food(request, restaurantId, foodId):
    if request.method == 'GET':
        queryset = models.Food.objects.filter(restaurant_id=restaurantId, pk=foodId)
        if queryset.exists():
            return utils.eatDDJsonResponse(food_to_dict(queryset.first()))
        else:
            return HttpResponse("Not exist", status=404)
    elif request.method == 'DELETE':
        queryset = models.Food.objects.filter(restaurant_id=restaurantId, pk=foodId)
        if queryset.exists():
            queryset.delete()
            return HttpResponse('Deleted!', status=200)
        else:
            return HttpResponse('This Food did not exist', status=405)
    return HttpResponse(restaurantId, status=200)


@require_http_methods(["POST"])
@eatdd_login_required
def create_food(request, restaurantId):
    received_data = json.loads(request.body.decode('utf-8'))
    new_food = models.Food(name=received_data['food_name'],
                           description=received_data['description'],
                           price=received_data['price'],
                           image=received_data['image'],
                           priority=received_data['priority'],
                           restaurant_id=restaurantId)
    new_food.save()
    return utils.eatDDJsonResponse(food_to_dict(new_food))


@require_http_methods(["GET"])
def get_menu(request, restaurantId):
    queryset = models.Food.objects.filter(restaurant_id=restaurantId)
    return utils.eatDDJsonResponse({"foods":food_queryset_to_array(queryset)})


def food_to_dict(new_food):
    return {
        "food_id": new_food.pk,
        "food_name": new_food.name,
        "description": new_food.description,
        "price": new_food.price,
        "priority": new_food.priority,
        "image": new_food.image
    }

def food_queryset_to_array(queryset):
    foods = []
    for item in queryset:
        foods.append(food_to_dict(item))
    return foods