from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('tasks/', views.tasks, name="tasks"),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutuser, name="logout"),
    path('register/', views.register, name="register"),
    path('createtask/', views.createtask, name="createtask"),
    path('edittask/<str:pk>/', views.edittask, name="edittask"),
    path('delete/<str:pk>/', views.deletetask, name="delete"),
    path('taskdetails/<str:pk>/', views.taskdetails, name="taskdetails")
]
