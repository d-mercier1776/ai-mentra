from django.db import models
from django.utils import timezone
from .classroom import ClassRoom
from .coding import Coding  # Assuming you have a Coding model

class Feedback(models.Model):
    begin_sec: models.DateTimeField = models.DateTimeField(null=False)
    end_sec: models.DateTimeField = models.DateTimeField(null=False)
    script: models.TextField = models.TextField(null=False)

    # Store coding as ForeignKey (or JSONField if it needs full object storage)
    coding: models.ForeignKey = models.ForeignKey(
        Coding,
        on_delete=models.CASCADE,
        related_name='feedbacks'
    )

    class_room: models.ForeignKey = models.ForeignKey(
        ClassRoom,
        on_delete=models.CASCADE,
        related_name='feedbacks'
    )

    m_datetime: models.DateTimeField = models.DateTimeField(default=timezone.now)
    r_datetime: models.DateTimeField = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Feedback for {self.class_room.class_room_name}'
