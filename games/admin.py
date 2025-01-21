from django.contrib import admin
from .models import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'created_at', 'updated_at')  # Replace 'name' with 'title'
    search_fields = ('title', 'description')  # Allow searching by title and description
    list_filter = ('created_at', 'updated_at')  # Add filters for created and updated times

