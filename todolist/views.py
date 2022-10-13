from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse
from .forms import TaskForm
from .models import Task
import datetime


@login_required(login_url='/todolist/login/')
def show_task(request):
    tasks = Task.objects.filter(user=request.user)
    context = {
        'page_title': 'To Do List',
        'tasks': tasks,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, 'todolist.html', context)

@login_required(login_url='/todolist/login/')
def show_task_json(request):
    tasks = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", tasks))

def create(request):
    task_form = TaskForm()

    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        form = task_form.save(commit=False)
        form.user = request.user
        form.save()

        return HttpResponseRedirect('/todolist/') 

    context = {
        'page_title': 'Create Task',
        'task_form': task_form
    }

    return render(request, 'create.html', context)

@login_required(login_url='/todolist/login/')
def addTask(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")

        new_task = Task(user=request.user, title=title, description=description)
        new_task.save()
        
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {
        'page_title': 'Register new user',
        'form': form
    }

    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:index"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response
    
@login_required(login_url='/todolist/login/')
def delete(request, delete_id):
    if (Task.objects.get(pk=delete_id).user == request.user):
        Task.objects.filter(pk=delete_id).delete()
    return redirect("todolist:index")
