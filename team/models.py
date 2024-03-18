from django.db import models
from django.contrib.auth.models import User


class TeamModel(models.Model):
    members = models.ManyToManyField(User, related_name='team_members', blank=True)
    team_admin = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name