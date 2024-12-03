from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication
from dating_API.settings import TOKEN_HEADER
from .models import Token


class TokenAuthentication(BaseAuthentication):

    def authenticate(self, request):
        key = request.META.get('HTTP_AUTHORIZATION', None)
        if key:
            key = key.split()[-1]
        user = get_user_model().objects.all()[0]
        try:
            token = Token.objects.get(key=key)
            return token.user, token
        except:
            return None, None
