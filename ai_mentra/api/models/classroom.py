from django.db import models
from django.utils import timezone
from .user import UserProfile

class ClassRoom(models.Model):
    class_room_name: models.CharField = models.CharField(max_length=200, null=False)
    teacher_name: models.CharField = models.CharField(max_length=150, null=False)  
    grade_level: models.CharField = models.CharField(max_length=50, null=False)
    subject: models.CharField = models.CharField(max_length=100, null=False)
    period: models.CharField = models.CharField(max_length=50, null=False)
    created_at: models.DateTimeField = models.DateTimeField(default=timezone.now)
    duration_class_time: models.IntegerField = models.IntegerField(null=False)
    language: models.CharField = models.CharField(max_length=50, null=False)

    m_datetime: models.DateTimeField = models.DateTimeField(default=timezone.now)
    r_datetime: models.DateTimeField = models.DateTimeField(default=timezone.now)
    removed: models.BooleanField = models.BooleanField(default=False)
    video_file_name: models.CharField = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.class_room_name
