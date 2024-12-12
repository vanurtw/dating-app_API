from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import TelegramUser, Profile
from rest_framework.generics import GenericAPIView
from .serializers import TelegramUserSerializers
from .models import Token
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.

UserSchema = openapi.Schema(type=openapi.TYPE_OBJECT,
                            properties={'token': openapi.Schema(description='тоекен', type=openapi.TYPE_STRING)})


class LoginAPIView(GenericAPIView):
    serializer_class = TelegramUserSerializers

    @swagger_auto_schema(
        responses={
            201: openapi.Response(description='Токен создан успешно', schema=UserSchema)
        }

    )
    def post(self, request):
        if not request.data.get('username'):
            return Response({"detail": "username обязательное поле"}, status=status.HTTP_400_BAD_REQUEST)
        teleg_user = TelegramUser.objects.filter(id_user=request.data.get('id_user'))
        serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        teleg_user = serializer.save(data=request.data, teleg_user=teleg_user)
        try:
            token = Token.objects.create(user=teleg_user)
        except IntegrityError as ex:
            tkn = Token.objects.get(user=teleg_user)
            tkn.delete()
            token = Token.objects.create(user=teleg_user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
