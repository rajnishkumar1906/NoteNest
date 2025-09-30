from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Note

@login_required(login_url='login')
def notesApp(request):
    if request.method == 'POST':
        subject = request.POST.get('subject').strip()
        topic = request.POST.get('topic').strip()
        note_content = request.POST.get('note').strip()

        if subject and topic and note_content:
            Note.objects.create(
                user=request.user,
                subject=subject,
                topic=topic,
                note=note_content
            )
            messages.success(request, 'Note saved successfully!')
        else:
            messages.error(request, 'All fields are required!')
        return redirect('notesApp')

    return render(request, 'notesApp.html')

@login_required(login_url='login')
def notes(request):
    user_notes = Note.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'notes.html', {'notes': user_notes})

@login_required(login_url='login')
def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)  # ensure only owner can delete
    if request.method == 'POST':
        note.delete()
        messages.success(request, 'Note deleted successfully!')
    return redirect('notes')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        first_name = request.POST.get('first_name').strip()
        last_name = request.POST.get('last_name').strip()
        email = request.POST.get('email').strip()
        password = request.POST.get('password').strip()
        password2 = request.POST.get('password2').strip()

        if password != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.save()
        messages.success(request, 'Registration successful. You can now log in.')
        return redirect('login')

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        login_input = request.POST.get('username').strip()  # email or username
        password = request.POST.get('password').strip()

        try:
            user_obj = User.objects.get(email=login_input)
            username = user_obj.username
        except User.DoesNotExist:
            username = login_input

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('notesApp')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'login.html')

@login_required(login_url='login')
def logout_view(request):
    auth_logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('login')
