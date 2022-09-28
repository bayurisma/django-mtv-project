from django.urls import path
from . import views

app_name = 'todolist'
urlpatterns = [
    path('', views.show_task, name='index'),
    path('create-task/', views.create, name='create-task'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]