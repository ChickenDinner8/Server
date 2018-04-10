from django.http import HttpResponse


def boss(request):
    return HttpResponse("Hello Boss")


def customer(request):
    return HttpResponse("Hello Customer")
