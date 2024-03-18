from rest_framework import viewsets
from .models import ScheduleModel
from . import serializers
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from rest_framework import status

# Create your views here.

class ScheduleModelViewset(viewsets.ModelViewSet):
    queryset = ScheduleModel.objects.all()
    serializer_class = serializers.ScheduleModelSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']


    # def get_queryset(self):
    #     user = self.request.user
    #     return ScheduleModel.objects.filter(user=user).order_by('datetime')





# class UpcomingScheduleAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         user = request.user

#         # Retrieve upcoming or reminder schedules
#         now = timezone.now()
#         upcoming_schedules = ScheduleModel.objects.filter(
#             user=user,
#             reminder_time__isnull=False,
#             reminder_time__gt=now
#         ).order_by('reminder_time')[:5]  # You can adjust the number of schedules to retrieve

#         # Serialize the data
#         serializer = serializers.ScheduleModelSerializer(upcoming_schedules, many=True)

#         return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    
# class ScheduleCountView(APIView):
#     def get(self, request, format=None):
#         schedule_count = ScheduleModel.objects.count()
#         serializer = serializers.ScheduleCountSerializer({'schedule_count': schedule_count})
#         return Response(serializer.data)

