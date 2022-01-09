from django.contrib import admin
from podcasts.models import Episodes

@admin.register(Episodes)
class EpisodesAdmin(admin.ModelAdmin):
    class Media:
        js = ('/static/js/tinyInject.js',)

