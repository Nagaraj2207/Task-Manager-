"""
URL configuration for taskmanager_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path("register/", views.user_registration, name="register"),
    path("login/", views.user_login, name="login"),
    path("login/forgot_password/",views.forget_pass, name="forgot_password"),
    path("login/task_app_home/", views.task_app_home, name="task_app_home"),
    path("login/task_app_home/update_user/", views.update_user, name="update_user"),
    path("login/task_app_home/update_user/change_password/", views.change_password, name="change_password"),
    path("login/task_app_home/add_task/",views.add_task, name="add_task"),
    path("login/task_app_home/view_task/", views.view_task, name="view_task"),
    path("login/task_app_home/update_task/<int:id>/",views.update_task, name="update_task"),
    path("login/task_app_home/delete_task/<int:id>/",views.delete_task, name="delete_task"),
    ]
