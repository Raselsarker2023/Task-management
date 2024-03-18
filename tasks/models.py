from django.db import models
from categories.models import Category
from team.models import TeamModel
from django.contrib.auth.models import User
from .constants import STATUS_CHOICES, PRIORITY_CHOICES

# Create your models here.
    
class TaskModel(models.Model):
    admin_name = models.ForeignKey(User, related_name='admin_tasks', on_delete=models.CASCADE, null=True, blank=True)
    assigned_to = models.ForeignKey(User, related_name='assigned_tasks', on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    team_name = models.OneToOneField(TeamModel, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    daily_target = models.IntegerField(default=1, null=True, blank=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='1', blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=True)
    Cancel_reason = models.CharField(max_length=10, blank=True)


    def __str__(self):
        return self.title