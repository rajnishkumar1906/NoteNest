"""
URL configuration for Hello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include

# Customizing the admin site headers
admin.site.site_header = "Rajnish Icecreams"
admin.site.site_title = "My Custom Admin Portal"
admin.site.index_title = "Welcome to authentications"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('NotesApp.urls')),  # NotesApp URLs
]
