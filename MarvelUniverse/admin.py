from django.contrib import admin
from .models.marvel_models import Character, Comic, Series, CharacterInComic, CharacterInSeries
from .models.comment_models import SeriesReview
# Register your models here.
admin.site.register(Character)
admin.site.register(Comic)
admin.site.register(Series)
admin.site.register(CharacterInComic)
admin.site.register(CharacterInSeries)
admin.register(SeriesReview)

@admin.register(SeriesReview)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'series', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

