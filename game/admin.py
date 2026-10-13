from django.contrib import admin

from .models import GameData


@admin.register(GameData)
class GameDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')
    search_fields = ('user__username',)
    readonly_fields = ('created_at', 'updated_at')
