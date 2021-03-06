from django.contrib import admin

from .models import Tweet


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'search_term',
        'sentiment',
        'created',
        'modified',
    )
    list_filter = (
        'search_term',
        'sentiment',
    )
    search_fields = (
        'text',
    )
