from django.contrib import admin
from .models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'href', 'source', 'wrote_at', 'human_classification', 'parsed_at'
    )
    search_fields = (
        'title', 'source'
    )
    list_filter = ('wrote_at',)
    list_editable = ('human_classification',)
    list_display_links = ('id','title', )

class ThemeAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name')

class SourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','theme')
    search_fields = ('name',)

class SignAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Sign, SignAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(Theme, ThemeAdmin)
