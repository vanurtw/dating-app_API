from django.contrib import admin
from .models import Categories, TelegramUser


# Register your models here.
@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'create_date']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['create_date']
