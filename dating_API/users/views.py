from django.shortcuts import render
from django.template.context_processors import request
from rest_framework.generics import GenericAPIView
from rest_framework import permissions, status
from rest_framework.response import Response

from .models import Profile, LikeUser
from .serializers import ProfileSerializer
import random
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from auth_user.serializers import TelegramUserSerializers


# Create your views here.


class TestAPIView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, *args, **kwargs):
        return Response('ok')


class FormAPIView(GenericAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('id_latest', openapi.IN_QUERY, type=openapi.TYPE_INTEGER,
                              description='id последней анкеты'),
            openapi.Parameter('city', openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description='город slug'),
            openapi.Parameter('gender', openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description='гендер М/Ж')
        ]

    )
    def get(self, request, *args, **kwargs):
        city = request.GET.get('city', None)
        gender = request.GET.get('gender', None)
        id_latest = request.GET.get('id_latest')
        user_profile = request.user.profile_user_teleg
        user_profile_interests = user_profile.interests.all()
        query_profile_filter = Profile.objects.filter(~Q(id=user_profile.id)).order_by('id')
        if id_latest:
            query_profile_filter = query_profile_filter.filter(id__gt=id_latest)
        if city:
            query_profile_filter = query_profile_filter.filter(city__slug=city)
        if gender:
            query_profile_filter = query_profile_filter.filter(gender=gender)

        # КОСТЫЛЬ
        if user_profile_interests:
            qs = list()
            for i in query_profile_filter:
                for j in i.interests.all():
                    if j in user_profile_interests:
                        qs.append(i)
                        break

            serializer = self.get_serializer(qs[:10], many=True,
                                             context={'user_profile_interests': user_profile_interests,
                                                      'user_teleg': request.user})
            return Response(serializer.data)

        profile = query_profile_filter[:10]
        serializer = self.get_serializer(profile, many=True, context={'user_profile_interests': user_profile_interests,
                                                                      'user_teleg': request.user})
        return Response(serializer.data)


class LikeAPIView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('id_profile', openapi.IN_QUERY, type=openapi.TYPE_INTEGER,
                              description='id понравившейся анкеты'),
            openapi.Parameter('action', openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description='действие')
        ]
    )
    def get(self, request, *args, **kwargs):
        id_like_profile = request.GET.get('id_profile', None)
        action = request.GET.get('action', 'like')
        if not id_like_profile or not action:
            return Response({'detail': 'Не переданы параметры запроса'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            likes = request.user.user_teleg_likes.filter(like_profile_id=id_like_profile).exists()
            if likes:
                return Response({'detail': 'Вы уже добавили эту анкету в поравившиеся'},
                                status=status.HTTP_400_BAD_REQUEST)
            LikeUser.objects.create(user_teleg=request.user, like_profile_id=id_like_profile)
            return Response({'detail': 'анкета дабавлена в понравившиеся'}, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({'detail': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class MyProfileAPIView(GenericAPIView):
    pass


class MyMatchesAPIView(GenericAPIView):
    serializer_class = TelegramUserSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user_likes = request.user.user_teleg_likes.all()
        user_to_like = request.user.profile_user_teleg.user_profile_likes.all()
        qs_user_teleg = [i.like_profile.user_teleg for i in user_likes]
        qs = user_to_like.filter(user_teleg__in=qs_user_teleg)
        serializer = self.get_serializer([i.user_teleg for i in qs], many=True)
        return Response(serializer.data)
