from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import TelegramUser
from rest_framework.generics import GenericAPIView
from .serializers import TelegramUserSerializers
from .models import Token
from rest_framework import status


# Create your views here.


class LoginAPIView(GenericAPIView):
    serializer_class = TelegramUserSerializers

    def post(self, request):
        try:
            teleg_user = TelegramUser.objects.get(id_user=request.data.get('id_user'))
        except ObjectDoesNotExist as ex:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            teleg_user = serializer.save()
        try:
            token = Token.objects.create(user=teleg_user)
        except IntegrityError as ex:
            return Response('Токен уже создан для этого пользователя', status=status.HTTP_400_BAD_REQUEST)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
