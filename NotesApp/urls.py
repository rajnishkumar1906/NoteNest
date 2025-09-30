from django.urls import path
from . import views

urlpatterns = [
    path('', views.notesApp, name='notesApp'), 
    path('notes/', views.notes, name='notes'),
    path('delete/<int:pk>/', views.delete_note, name='delete_note'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
