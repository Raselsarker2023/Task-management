from rest_framework import serializers
from . import models

class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectModel
        fields = '__all__'
        
        # def create(self, validated_data):
        #     user = self.context['request'].user
        #     validated_data['user'] = user
        #     return super().create(validated_data)
        
        
    
# count serializers
class CountSerializer(serializers.Serializer):
    project_count = serializers.IntegerField()
    schedule_count = serializers.IntegerField()
    task_count = serializers.IntegerField()
    team_count = serializers.IntegerField()
