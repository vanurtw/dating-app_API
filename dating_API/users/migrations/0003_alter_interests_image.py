# Generated by Django 5.1.3 on 2024-12-03 16:41

import django.core.validators
import service.service
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_gender_alter_interests_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interests',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=service.service.loading_interests_images, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'webp'])], verbose_name='изображение'),
        ),
    ]
