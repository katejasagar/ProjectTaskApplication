"""AawazTask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from Projects.views import (ProjectView, TaskView, ProjectTaskView, AllTaskView, 
                            ProjectUpdateDeleteView, TaskUpdateDeleteView)
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', ProjectView.as_view(), name='project-list'),
    path('tasks/', AllTaskView.as_view(), name='task-list'),
    path('projects/<int:pk>/', ProjectTaskView.as_view(), name='project-task-list'),
    path('projects/<int:rk>/tasks/<int:pk>/', TaskView.as_view(), name='task-list'),
    path('projects/<int:pk>/update/', ProjectUpdateDeleteView.as_view(), name = 'project-update'),
    path('tasks/<int:pk>/update/', TaskUpdateDeleteView.as_view(), name = 'task-update'),
   
]
