from rest_framework import viewsets
from . import serializers
from rest_framework import filters
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import ProjectModel
from schedule. models import ScheduleModel
from tasks. models import TaskModel
from team. models import TeamModel
from .models import ProjectModel
from schedule .serializers import ScheduleModelSerializer
from tasks .serializers import TaskModelSerializer
from .serializers import ProjectModelSerializer
from django.utils import timezone
from . import serializers


class ProjectModelAPIView(viewsets.ModelViewSet):
    queryset = ProjectModel.objects.all()
    serializer_class = serializers.ProjectModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'admin_name__username', 'priority', 'abandon_reason']
    

    # def get_queryset(self):
    #     user = self.request.user
    #     queryset = ProjectModel.objects.filter(admin_name=user).order_by('priority')
    #     return queryset


    
        

# List API views

class ShortScheduleProjectTaskList(APIView):
    def get(self, request, *args, **kwargs):
        try:
            user = request.user
            
            now = timezone.now()

            # Fetch upcoming schedules, projects, and tasks
            upcoming_schedules = ScheduleModel.objects.filter(
                created_by=user,
                reminder_time__isnull=False,
                reminder_time__gt=now
            ).order_by('reminder_time')[:5]

            projects = ProjectModel.objects.filter(
                created_by=user,
                end_date__gt=now
            ).order_by('end_date')[:5]

            tasks = TaskModel.objects.filter(
                user_name=user,  
                end_date__gt=now
            ).order_by('end_date')[:5]


            # Serialize the data
            upcoming_schedules_data = ScheduleModelSerializer(upcoming_schedules, many=True).data
            projects_data = ProjectModelSerializer(projects, many=True).data
            tasks_data = TaskModelSerializer(tasks, many=True).data

            return Response({
                'upcoming_schedules': upcoming_schedules_data,
                'projects': projects_data,
                'tasks': tasks_data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





# count view 
class CountView(APIView):
    def get(self, request, format=None):
        project_count = ProjectModel.objects.count()
        schedule_count = ScheduleModel.objects.count()
        task_count = TaskModel.objects.count()
        team_count = TeamModel.objects.count()

        data = {
            'project_count': project_count,
            'schedule_count': schedule_count,
            'task_count': task_count,
            'team_count': team_count,
        }

        serializer = serializers.CountSerializer(data)
        return Response(serializer.data)
