from django.http import HttpResponse

'''
Personlized require_login decorator
'''
def eatdd_login_required(func):
    def check_login_status(request):
        if "username" in request.session:
            # Already Log In
            return func(request)
        else:
            # Not Log In
            return HttpResponse("Not Log In", status=401)
    return check_login_status