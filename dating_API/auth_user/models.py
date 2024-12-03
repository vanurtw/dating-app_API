import binascii
import os
from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import TelegramUser


class Token(models.Model):
    '''
    Модель токена авторизации по умолчанию.
    '''
    key = models.CharField(_("Key"), max_length=40, primary_key=True)
    user = models.OneToOneField(
        TelegramUser, related_name='auth_token',
        on_delete=models.CASCADE, verbose_name=_("User")
    )
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(20)).decode()

    # objects = models.Manager()
    def __str__(self):
        return self.key
