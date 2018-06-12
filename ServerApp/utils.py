from django.http import HttpResponse
import json
BOSS_USERNAME='username'

def eatDDJsonResponse(obj):
    return HttpResponse(json.dumps(obj), content_type="application/json")