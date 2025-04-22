from rest_framework.authentication import SessionAuthentication

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class CustomSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
       pass



@api_view(['GET'])
@login_required
def is_authenticated(request):
    """
    check whether user is authorized
    """
    return Response({'isAuthenticated': True})