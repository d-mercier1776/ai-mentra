# api/models/user_profile.py
from django.db import models
from django.contrib.auth.models import User  # Django's default
from django.utils import timezone

class UserProfile(models.Model):
    user: models.OneToOneField = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_school:models.CharField = models.CharField(max_length=150, null=False)
    profile_picture_url:models.URLField = models.URLField(null=True, blank=True)
    temp_password:models.BooleanField = models.BooleanField(null=True, blank=True)
    m_datetime:models.DateTimeField = models.DateTimeField(default=timezone.now)
    r_datetime:models.DateTimeField = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username
