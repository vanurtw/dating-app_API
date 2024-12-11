from django.template.context_processors import request
from rest_framework import serializers
from .models import Profile, Categories, Interests, LikeUser
from auth_user.serializers import TelegramUserSerializers


class InterestSerializer(serializers.ModelSerializer):
    coincidence = serializers.SerializerMethodField()

    def get_coincidence(self, obj):
        interests = self.context.get('user_profile_interests')
        return obj in interests

    class Meta:
        model = Interests
        fields = ['title', 'image', 'slug', 'coincidence']


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
