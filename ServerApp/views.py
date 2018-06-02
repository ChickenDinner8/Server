from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.http import require_http_methods
import json
from . import models

@require_http_methods(["GET", "POST", "DELETE"])
def login(request):
    received_data = json.loads(request.body)
    if request.method == 'POST':
        try:
            user = models.BusinessUser.objects.get(username=received_data['username'], password=received_data['password'])
            request.session['username'] = user.username
            return HttpResponse('Log In')
        except Exception as err:
            print(err)
            return HttpResponse('Error LogIn', status=400)

@require_http_methods(["GET", "POST", "PUT"])
def bossUserAdmin(request):
    # Create a user
    if request.method == "POST":
        received_data = json.loads(request.body)
        newUser = models.BusinessUser(username=received_data['username'], password=received_data['password'])
        try:
            newUser.save(force_insert=True)
        except:
            return HttpResponse("Duplicate Username", status=400)
        # print (received_data)
        return HttpResponse("Regist new user successful!")
    elif request.method == "GET":
        try:
            username = request.session['username']
            user = models.BusinessUser.objects.get(username=username)
            return HttpResponse(username)
        except:
            return HttpResponse("Not Log In", status=400)
    elif request.method == "PUT":
        pass

def boss(request):
    return render_to_response("index.html")


def customer(request):
    return HttpResponse("Hello Customer")


def sendJsonData(msg, status_code=200):
    return HttpResponse(msg, content_type="application/json", status=status_code)