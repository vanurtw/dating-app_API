from django.core.validators import FileExtensionValidator
from django.db import models
from service.service import loading_interests_images, loading_profile_images


# Create your models here.
class TelegramUser(models.Model):
    '''
    Модель пользователя телеграмм аккаунта
    '''
    id_user = models.CharField('id пользов. аккаунта телеграмма', unique=True, max_length=12)
    is_bot = models.BooleanField('бот', default=False)
    first_name = models.CharField('имя', max_length=100, blank=True, null=True)
    last_name = models.CharField('фамилия', max_length=100, blank=True, null=True)
    username = models.CharField('username', max_length=100)
    create_date = models.DateField('дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Пользователя телеграмма'
        verbose_name_plural = 'Пользователи телеграмма'

    def __str__(self):
        return f'{self.username}_{self.id_user}'

    is_authenticated = True


class Categories(models.Model):
    '''
    Модель категорий для интересов
    '''
    title = models.CharField('название', max_length=25)
    slug = models.CharField(max_length=100)
    create_date = models.DateField('дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Категорию интереса'
        verbose_name_plural = 'Категории интересов'

    def __str__(self):
        return self.title


class Interests(models.Model):
    '''
    Модель интересов связанных с категориями
    '''
    title = models.CharField('название', max_length=25)
    image = models.ImageField(
        verbose_name='изображение',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'webp'])],
        upload_to=loading_interests_images,
        blank=True,
        null=True
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
    '''
    Модель городов
    '''
    title = models.CharField('город', max_length=25)
    create_date = models.DateField('дата создания', auto_now_add=True)
    slug = models.CharField(max_length=75)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.title


class Profile(models.Model):
    '''
    Модель профиля пользователя телеграмм аккаунта
    '''
    CHOICES = [
        ('М', 'Мужской'),
        ('Ж', 'Женский'),
    ]
    user_teleg = models.OneToOneField(
        TelegramUser,
        on_delete=models.CASCADE,
        related_name='profile_user_teleg',
        verbose_name='пользователь телеграм. аккаунта'
    )
    gender = models.CharField(max_length=3, choices=CHOICES, default='М')
    city = models.ForeignKey(
        Cities,
        on_delete=models.CASCADE,
        related_name='city_profiles',
        verbose_name='город',
        blank=True, null=True
    )
    description = models.CharField(
        'описание',
        max_length=300,
        help_text='расскажи о себе',
        blank=True,
        null=True
    )
    interests = models.ManyToManyField(
        Interests,
        related_name='interest_profiles',
        verbose_name='интересы',
        blank=True,
        null=True
    )
    films = models.CharField(
        'фильмы',
        max_length=50,
        blank=True,
        null=True
    )
    books = models.CharField(
        'книги',
        max_length=50,
        blank=True,
        null=True
    )
    create_date = models.DateField('дата создания', auto_now_add=True)

    def __str__(self):
        return f'{self.user_teleg}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class ProfileImages(models.Model):
    '''
    Модель изображений прикрепленных к профилю
    '''
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='profile_images',
        verbose_name='профиль'
    )
    image = models.ImageField(
        verbose_name='изображение',
        upload_to=loading_profile_images,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])]
    )
    create_date = models.DateField('дата создания', auto_now_add=True)

    def __str__(self):
        return self.profile

    class Meta:
        verbose_name = 'Изображения профиля'
        verbose_name_plural = 'Изображение профиля'
