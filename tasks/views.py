from rest_framework import viewsets
from . models import TaskModel
from . import serializers
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class TaskModelViewset(viewsets.ModelViewSet):
    queryset = TaskModel.objects.all()
    serializer_class = serializers.TaskModelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description', 'priority', 'status']

        
        
    # def get_queryset(self):
    #     user = self.request.user
    #     queryset = TaskModel.objects.filter(user=user).order_by('priority')
    #     return queryset