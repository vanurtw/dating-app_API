# Generated by Django 5.1.3 on 2024-12-02 18:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='image',
        ),
        migrations.AddField(
            model_name='categories',
            name='create_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='дата создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='create_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='дата создания'),
            preserve_default=False,
        ),
    ]