from lib2to3.fixes.fix_input import context

from django.template.context_processors import request
from rest_framework import serializers
from .models import Profile, Categories, Interests, LikeUser, Cities
from auth_user.serializers import TelegramUserSerializers


class InterestSerializer(serializers.ModelSerializer):
    coincidence = serializers.SerializerMethodField()

    def get_coincidence(self, obj):
        interests = self.context.get('user_profile_interests')
        return obj in interests

    class Meta:
        model = Interests
        fields = ['title', 'image', 'slug', 'coincidence']


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ['id', 'title', 'slug']


class ProfileInterestSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=False)

    class Meta:
        model = Interests
        fields = ['id', 'title', 'image', 'slug']


class ProfileSerializer(serializers.ModelSerializer):
    interests = InterestSerializer(many=True)
    city = serializers.SerializerMethodField()
    reciprocity = serializers.SerializerMethodField()
    user_teleg = TelegramUserSerializers()

    def get_city(self, obj):
        return obj.city.title

    def get_reciprocity(self, obj, *args, **kwargs):
        user_teleg = self.context.get('user_teleg')
        likes = LikeUser.objects.filter(user_teleg=user_teleg, like_profile=obj)
        return likes.exists()

    class Meta:
        model = Profile
        fields = ['id', 'gender', 'age', 'city', 'description', 'films', 'books', 'reciprocity', 'user_teleg',
                  'interests', 'create_date']


class MyProfileSerializer(serializers.ModelSerializer):
    city = CitiesSerializer()
    interests = ProfileInterestSerializer(many=True)

    class Meta:
        model = Profile
        fields = ['id', 'gender', 'age', 'city', 'description', 'films', 'books', 'user_teleg',
                  'interests', 'create_date']
        depth = 1


class CategoriesInterestsSerializer(serializers.Serializer):

    def to_representation(self, instance):
        interests = instance.interests_categories.all()
        user_profile_interests = self.context.get('user_profile_interests')
        serializer = InterestSerializer(interests, context={'user_profile_interests': user_profile_interests}, many=True)
        return {instance.title: serializer.data}
