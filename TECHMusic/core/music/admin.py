from django.contrib import admin
from . import models
from django.utils.html import format_html, mark_safe



@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_html_img']

    def get_html_img(self, object):
        if object.preview_img:
            return mark_safe(f"<img src='{object.preview_img.url}' height='100'>")
        return 'Обложка пуста'

@admin.register(models.Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_html_img', 'audio_player', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)

    def audio_player(self, obj):
        if obj.file:
            return format_html(
                '<audio controls style="width: 300px;">'
                '<source src="{}" type="audio/mpeg">'
                'Your browser does not support the audio element.'
                '</audio>',
                obj.file.url
            )
        return "Нет файла"

    def get_html_img(self, object):
        if object.img:
            return mark_safe(f"<img src='{object.img.url}' height='60'>")
        return 'Обложка пуста'

    audio_player.short_description = "Аудиоплеер"