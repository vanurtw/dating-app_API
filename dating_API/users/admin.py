from django.contrib import admin
from .models import (Categories,
                     TelegramUser,
                     Interests,
                     Cities,
                     Profile,
                     ProfileImages
                     )


# Register your models here.
@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'create_date']
    list_display_links = ['id', 'username']
    list_filter = ['create_date']


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'create_date']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['create_date']


@admin.register(Interests)
class InterestsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'create_date']
    list_display_links = ['id', 'title']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['create_date']


@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['create_date']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_teleg__username', 'create_date']
    list_display_links = ['id', 'user_teleg__username']
    list_filter = ['city', 'create_date']

@admin.register(ProfileImages)
class ProfileImages(admin.ModelAdmin):
    list_display = ['id', 'profile', 'create_date']
    list_display_links = ['id', 'profile']


