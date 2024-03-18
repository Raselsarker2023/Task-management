from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.filters import SearchFilter
# from rest_framework.permissions import IsAuthenticated
from .models import TeamModel


# Create your views here.

class TeamModelViewset(viewsets.ModelViewSet):
    queryset = models.TeamModel.objects.all()
    serializer_class = serializers.TeamModelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']
    
    
    # def get_queryset(self):
    #     user = self.request.user
    #     queryset = TeamModel.objects.filter(creator=user)
    #     return queryset
    