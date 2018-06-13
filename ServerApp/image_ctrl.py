from ServerApp import models
from django.http import HttpResponse
from .auth_required_decorator import eatdd_login_required
from . import utils
from django.views.decorators.http import require_http_methods
from django.core.files.storage import FileSystemStorage


@require_http_methods(["POST"])
@eatdd_login_required
def upload_image(request):
    print(request)
    print(type(request.FILES['image']))
    image_file = request.FILES['image']
    fs = FileSystemStorage()
    filename = fs.save(image_file.name, image_file)
    url = fs.url(filename)
    return utils.eatDDJsonResponse({'url': '/static/upload_image/' + url})
