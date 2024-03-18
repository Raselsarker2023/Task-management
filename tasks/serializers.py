from rest_framework import serializers
from . import models


class TaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TaskModel
        fields = '__all__'
        
        
class TaskCountSerializer(serializers.Serializer):
    task_count = serializers.IntegerField()