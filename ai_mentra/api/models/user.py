from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, user_name, user_school, password=None, **extra_fields):
        if not email:
            raise ValueError('Email must be provided')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            user_name=user_name,
            user_school=user_school,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, user_name, user_school, password=None, **extra_fields):
        extra_fields.setdefault('admin', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, user_name, user_school, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    user_email: models.EmailField = models.EmailField(unique=True, null=False)
    profile_picture_url: models.URLField = models.URLField(null=False)
    user_password: models.CharField = models.CharField(max_length=128) 
    user_name: models.CharField= models.CharField(max_length=150, null=False)
    user_school: models.CharField = models.CharField(max_length=150, null=False)

    enabled:models.BooleanField = models.BooleanField(default=True)
    removed: models.BooleanField= models.BooleanField(default=False)
    admin: models.BooleanField= models.BooleanField(default=False)
    temp_password: models.BooleanField = models.BooleanField(null=True, blank=True)

    m_datetime: models.DateTimeField = models.DateTimeField(default=timezone.now)
    r_datetime: models.DateTimeField = models.DateTimeField(default=timezone.now)

    is_staff: models.BooleanField = models.BooleanField(default=False)
    is_active: models.BooleanField = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'user_email'
    REQUIRED_FIELDS = ['user_name', 'user_school']

    def __str__(self):
        return self.user_email
