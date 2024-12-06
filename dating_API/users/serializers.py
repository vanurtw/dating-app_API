from rest_framework import serializers
from .models import Profile, Categories, Interests


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


    def get_city(self, obj):
        return obj.city.title

    class Meta:
        model = Profile
        fields = ['id', 'gender', 'city', 'description', 'interests', 'films', 'books', 'create_date']
