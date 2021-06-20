from rest_framework import serializers
from .models import Projects
from .models import Tasks


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = (
            'project_id',
            'project_name',
            'description',
            'duration',
            'status',
            'image',

        )

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = (
            'task_id',
            'project_id',
            'task_name',
            'description',
            'start_date',
            'end_date',

        )