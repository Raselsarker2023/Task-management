from django.db import models
from django.contrib.auth.models import User
from categories.models import Category
from tasks.models import TaskModel
from team.models import TeamModel
from .constants import STATUS_CHOICES, PRIORITY_CHOICES


class ProjectModel(models.Model):
    admin_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    task_name = models.ManyToManyField(TaskModel, blank=True)
    team_name = models.ForeignKey(TeamModel, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='1', blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=True)
    abandon_reason = models.TextField(blank=True, max_length=255)
    daily_target = models.IntegerField(default=1, blank=True)


    def __str__(self):
        return self.name
    
    