from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('subject', 'topic', 'user', 'created_at')  # columns to display
    list_filter = ('user', 'created_at')  # filter sidebar
    search_fields = ('subject', 'topic', 'note')  # search box
