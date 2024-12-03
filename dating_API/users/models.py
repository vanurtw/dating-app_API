from django.core.validators import FileExtensionValidator
from django.db import models
from service.service import loading_interests_images


# Create your models here.
class TelegramUser(models.Model):
    '''Модель пользователя телеграмм аккаунта'''
    id_user = models.IntegerField('id пользов. аккаунта')
    is_bot = models.BooleanField('бот', default=False)
    first_name = models.CharField('имя', max_length=100)
    last_name = models.CharField('фамилия', max_length=100)
    username = models.CharField('username', max_length=100)
    create_date = models.DateField('дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Пользователи телеграмма'
        verbose_name_plural = 'Пользователи телеграмма'

    def __str__(self):
        return f'{self.username}_{self.id_user}'


class Categories(models.Model):
    '''Модель категорий для интересов'''
    title = models.CharField('название', max_length=25)
    slug = models.CharField(max_length=100)
    create_date = models.DateField('дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Категории интересов'
        verbose_name_plural = 'Категории интересов'

    def __str__(self):
        return self.title


class Interests(models.Model):
    '''Модель интересов связанных с категориями'''
    title = models.CharField('название', max_length=25)
    image = models.ImageField(
        verbose_name='изображение',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])],
        upload_to=loading_interests_images
    )
    category = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE,
        related_name='interests_categories',
        verbose_name='Категория'
    )
    slug = models.CharField(max_length=100)
    create_date = models.DateField('дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Интерес'
        verbose_name_plural = 'Интересы'

    def __str__(self):
        return self.title

class Cities(models.Model):
    '''Модель городов'''
    title = models.CharField('город', max_length=25)
    create_date = models.DateField('дата создания', auto_now_add=True)
    slug = models.CharField(max_length=75)

    class Meta:
        verbose_name = 'Города'
        verbose_name_plural = 'Город'

