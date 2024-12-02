from django.db import models


# Create your models here.
class TelegramUser(models.Model):
    '''Модель пользователя телеграмм аккаунта'''
    id_user = models.IntegerField('id пользов. аккаунта')
    is_bot = models.BooleanField('бот', default=False)
    first_name = models.CharField(max_length=100, )
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Пользоват. телеграмма'
        verbose_name_plural = 'Пользоват. телеграмма'

    def __str__(self):
        return f'{self.username}_{self.id_user}'

class Categories(models.Model):
    '''Модель категорий для интересов'''
    title = models.CharField('название', max_length=25)
    image = models.ImageField('изображение', upload_to='')

    class Meta:
        verbose_name = 'Категории интересов'
        verbose_name_plural = 'Категории интересов'