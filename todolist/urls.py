from django.urls import path
from . import views

app_name = 'todolist'
urlpatterns = [
    path('', views.show_task, name='index'),
    path('json/', views.show_task_json, name='show_json'),
    path('create-task/', views.create, name='create-task'),
    path('add/', views.addTask, name='add-task'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]