from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm


def home(request):
    context = {}
    return render(request, 'tasks/home.html', context)


def tasks(request):
    user_tasks = Task.objects.filter(user=request.user)

    search_query = request.GET.get('search', '')
    if search_query:
        user_tasks = user_tasks.filter(Q(title__icontains=search_query))

    due_date_filter = request.GET.get('due_date', '')
    if due_date_filter:
        user_tasks = user_tasks.filter(due_date__icontains=due_date_filter)

    priority_filter = request.GET.get('priority', '')
    if priority_filter:
        user_tasks = user_tasks.filter(priority=priority_filter)

    status_filter = request.GET.get('status', '')
    if status_filter:
        user_tasks = user_tasks.filter(status=status_filter)
    context = {'tasks': user_tasks}
    return render(request, 'tasks/tasks.html', context)


def taskdetails(request, pk):
    task = Task.objects.get(id=pk)
    if request.user != task.user:
        return HttpResponse("Unauthorized access")
    context = {'task': task}
    return render(request, 'tasks/taskdetails.html', context)


def createtask(request):
    if not request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks')
    else:
        form = TaskForm()
    context = {'form': form}
    return render(request, 'tasks/createtask.html', context)


def edittask(request, pk):
    task = Task.objects.get(id=pk)

    if request.user != task.user:
        return HttpResponse("Unauthorized access")

    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')

    else:
        form = TaskForm(instance=task)

    context = {'form': form}
    return render(request, 'tasks/edittask.html', context)


def deletetask(request, pk):
    task = Task.objects.get(id=pk)
    if request.user != task.user:
        return HttpResponse("Unauthorized access")
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    context = {'task': task}
    return render(request, 'tasks/delete.html', context)


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
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
    if request.user.is_authenticated:
        return redirect('home')
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
