from django.contrib import admin
from .models.marvel_models import Character, Comic, Series, CharacterInComic, CharacterInSeries
# Register your models here.
admin.site.register(Character)
admin.site.register(Comic)
admin.site.register(Series)
admin.site.register(CharacterInComic)
admin.site.register(CharacterInSeries)

