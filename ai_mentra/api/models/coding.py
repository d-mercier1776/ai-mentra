from django.db import models
from django.contrib.postgres.fields import JSONField  # if using PostgreSQL
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import timezone

class Coding(models.Model):
    coding_data = models.JSONField(encoder=DjangoJSONEncoder, null=False, default=dict)

    m_datetime:models.DateTimeField = models.DateTimeField(default=timezone.now)
    r_datetime:models.DateTimeField = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Coding {self.id}"
