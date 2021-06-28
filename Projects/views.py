from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import ProjectSerializer, TaskSerializer
from rest_framework import mixins
from rest_framework.response import Response
from .models import Projects, Tasks
# Create your views here.

class ProjectView( generics.ListCreateAPIView,  generics.GenericAPIView):
    serializer_class = ProjectSerializer
    queryset = Projects.objects.all()


class ProjectTaskView(APIView):
    def get(self, request, *args, **kwargs):
        param = kwargs
        qs = Tasks.objects.filter(project_id = param['pk'])
        qs1 = Projects.objects.filter(project_id = param['pk'])
        serializer = TaskSerializer(qs, many = True)
        serializer1 = ProjectSerializer(qs1, many = True)
        return Response(serializer1.data + serializer.data)

class AllTaskView(mixins.ListModelMixin, mixins.CreateModelMixin,  generics.GenericAPIView):
    serializer_class = TaskSerializer
    queryset = Tasks.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create( request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request,*args, **kwargs)

class TaskView(APIView):
    def get(self, request, *args, **kwargs):
        param = kwargs
        qs = Tasks.objects.filter(task_id = param['pk'])
        serializer = TaskSerializer(qs, many = True)
        qs1 = Projects.objects.filter(project_id = param['rk'])
        serializer1 = ProjectSerializer(qs1, many = True)
        if serializer.data[0]['project_id'] == serializer1.data[0]['project_id'] :
            return Response(serializer.data)
        else: 
            return Response('Projectid doesnot match')

class ProjectUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = Projects


class TaskUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Tasks


    