from django.http import HttpResponse
from django.shortcuts import render_to_response


def login(request):
    return HttpResponse("Please Login")


def boss(request):
    return render_to_response("index.html")


def customer(request):
    return HttpResponse("Hello Customer")
