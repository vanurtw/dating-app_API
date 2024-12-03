from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import TelegramUser
from rest_framework.generics import GenericAPIView
from .serializers import TelegramUserSerializers
from .models import Token

# Create your views here.


class LoginAPIView(GenericAPIView):
    serializer_class = TelegramUserSerializers

    def post(self, request):
        try:
            teleg_user = TelegramUser.objects.get(id_user=request.data.get('id_user'))
        except Exception as ex:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            teleg_user = serializer.save()
        token = Token.objects.create(user=teleg_user)
        return Response(token.key)
