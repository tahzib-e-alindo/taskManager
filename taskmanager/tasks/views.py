from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.http import HttpResponse
from .models import Task

# Create your views here.


def home(request):
    context = {}
    return render(request, 'tasks/home.html', context)


def tasks(request):
    user_tasks = Task.objects.filter(user=request.user)
    context = {'tasks': user_tasks}
    return render(request, 'tasks/tasks.html', context)


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User Does not exist")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tasks')
        else:
            messages.error(request, "Type correct Username & Password")
    context = {}
    return render(request, 'tasks/login.html', context)


def logoutuser(request):
    logout(request)
    return redirect('home')


def register(request):
    form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('tasks')
        else:
            messages.error(request, "Register error, Try Again")
    context = {'form': form}
    return render(request, 'tasks/register.html', context)
