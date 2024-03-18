from rest_framework import serializers
from . import models

class ScheduleModelSerializer(serializers.ModelSerializer):
    shortened_reminder = serializers.CharField(source='get_shortened_reminder', read_only=True)

    class Meta:
        model = models.ScheduleModel
        fields = '__all__'
        
        
class ScheduleCountSerializer(serializers.Serializer):
    schedule_count = serializers.IntegerField()
