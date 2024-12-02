from django.contrib import admin
from .models import Categories, TelegramUser, Interests


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
    pass