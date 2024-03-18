from django.db import models
from django.contrib.auth.models import User
from . constants import STATUS_CHOICES


class ScheduleModel(models.Model):
    admin_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    reminder_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=True, null=True)
    completed = models.BooleanField(default=False)
    cancel_reason = models.CharField(max_length=150, blank=True, null=True)
    
    
    def __str__(self):
        return self.title
    
    
    def get_shortened_reminder(self):
        if self.reminder_time:
            # You can customize the format as per your needs
            return self.reminder_time.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return None
    