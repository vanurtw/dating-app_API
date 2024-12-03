from rest_framework import serializers
from users.models import TelegramUser


class TelegramUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = ['id_user', 'is_bot', 'first_name', 'last_name', 'username', 'create_date']
