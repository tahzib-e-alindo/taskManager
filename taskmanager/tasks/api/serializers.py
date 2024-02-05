from rest_framework.serializers import ModelSerializer
from tasks.models import Task
from rest_framework import serializers


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
    image = serializers.ImageField()
