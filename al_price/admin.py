from django.contrib import admin

from .models import Settings

# Register your models here.
class SettingsAdmin(admin.ModelAdmin):
    list_display = ("allegro_path",)

admin.site.register(Settings, SettingsAdmin)