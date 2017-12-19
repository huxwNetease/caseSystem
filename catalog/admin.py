from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.WordMenu)
admin.site.register(models.PictureMenu)
admin.site.register(models.VoiceMenu)
admin.site.register(models.HomeMenu)