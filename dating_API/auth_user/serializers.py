from rest_framework import serializers
from users.models import TelegramUser, Profile


class TelegramUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = ['id_user', 'is_bot', 'first_name', 'last_name', 'username', 'image', 'create_date']


    def save(self, **kwargs):
        teleg_user=kwargs.get('teleg_user')
        if teleg_user:
            instance = teleg_user.update(**kwargs.get('data'))
            return teleg_user[0]
        else:
            instance = TelegramUser.objects.create(**kwargs.get('data').dict())
            Profile.objects.create(user_teleg=instance)
            return instance
