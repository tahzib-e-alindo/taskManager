from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('tasks/', views.tasks, name="tasks"),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutuser, name="logout"),
    path('register/', views.register, name="register")
]
