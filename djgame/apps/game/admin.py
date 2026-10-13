from djgame.apps.game.models.game_data import GameData
from django.contrib import admin


class GameDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'updated')
    search_fields = ('user__username',)
    readonly_fields = ('created', 'updated')


admin.site.register(GameData, GameDataAdmin)
