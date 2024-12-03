from django.contrib import admin
from .models import Token


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ['key']
    list_display_links = ['key']
    list_filter = ['created']
