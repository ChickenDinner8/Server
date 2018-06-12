from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.views.decorators.http import require_http_methods
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
import json
from ServerApp import models
from .auth_required_decorator import eatdd_login_required
from . import utils

@require_http_methods(["GET", "POST", "PUT"])
def req_restaurant(request):
    if 'username' not in request.session:
        return HttpResponse('Not Log In', status=400)
    username = request.session['username']

    if request.method == "POST":
        received_data = json.loads(request.body.decode('utf-8'))
        newRestaurant = models.Restaurant(name=received_data['name'],
                                          description=received_data['description'],
                                          image=received_data['image_url'],
                                          boss=models.BusinessUser.objects.get(username=username))

        if not models.Restaurant.objects.filter(name=newRestaurant.name).exists():
            newRestaurant.save(force_insert=True)
            return HttpResponse("Regist new restaurant successful!")
        else:
            return HttpResponse('fail', status=400)

    elif request.method == "GET":
        boss = models.BusinessUser.objects.get(username=username)
        queryset = models.Restaurant.objects.filter(boss=boss)
        if queryset.exists():
            return HttpResponse(queryset.first())
        else:
            return HttpResponse('fail', status=400)

    elif request.method == "PUT":
        pass

@require_http_methods(["GET"])
@eatdd_login_required
def get_all_restaurant(request):
    username = request.session[utils.BOSS_USERNAME]
    querset = models.Restaurant.objects.filter(boss__username=username)
    restaurants = []
    for item in querset:
        restaurants.append({
            "id":item.pk,
            "name":item.name,
            "location":item.description,
            "image":item.image
        })
    return utils.eatDDJsonResponse({"restaurants":restaurants})