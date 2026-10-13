from djgame.apps.game.models.game_data import GameData
from djgame.apps.game.models.game import Game
from django.contrib import admin


class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_active', 'updated')
    list_editable = ('is_active',)
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created', 'updated')

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        field = super().formfield_for_dbfield(db_field, request, **kwargs)
        if db_field.name == 'code':
            field.widget.attrs.update(rows=30, style='width: 100%; font-family: monospace;')
        return field


class GameDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'updated')
    list_filter = ('game',)
    search_fields = ('user__username',)
    readonly_fields = ('created', 'updated')


admin.site.register(Game, GameAdmin)
admin.site.register(GameData, GameDataAdmin)
