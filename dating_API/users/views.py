from django.shortcuts import render
from django.template.context_processors import request
from rest_framework.generics import GenericAPIView
from rest_framework import permissions
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
import random
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


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
                                             context={'user_profile_interests': user_profile_interests})
            return Response(serializer.data)

        profile = query_profile_filter[:10]
        serializer = self.get_serializer(profile, many=True, context={'user_profile_interests': user_profile_interests})
        return Response(serializer.data)


class LikeAPIView(GenericAPIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('id_profile', openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description='id анкеты'),
            openapi.Parameter('action', openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description='действие')
        ]
    )
    def get(self, request, *args, **kwargs):
        id_profile = request.GET.get('id_profile')
        action = request.GET.get('action')
