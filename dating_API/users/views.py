from lib2to3.fixes.fix_input import context

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
            openapi.Parameter('id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description='id текущей анкеты'),
            openapi.Parameter('city', openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description='город slug'),
            openapi.Parameter('gender', openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description='гендер М/Ж')
        ]

    )
    def get(self, request, *args, **kwargs):
        city = request.GET.get('city', None)
        gender = request.GET.get('gender', None)
        id = request.GET.get('id', None)
        user_profile = request.user.profile_user_teleg
        user_profile_interests = user_profile.interests.all()
        query_profile = Profile.objects.filter(~Q(id=user_profile.id), ~Q(id=id), city__slug=city, gender=gender)
        query_profile_filter = query_profile.filter(interests__in=user_profile_interests)
        profile = random.choices(query_profile_filter)[0]
        serializer = self.get_serializer(profile, context={'user_profile_interests': user_profile_interests})
        return Response(serializer.data)
