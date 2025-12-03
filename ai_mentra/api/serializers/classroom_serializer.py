from rest_framework import serializers
from api.models.classroom import ClassRoom

class ClassRoomSerializer(serializers.ModelSerializer):
    teacher = serializers.StringRelatedField()  # or PrimaryKeyRelatedField if you want ID

    class Meta:
        model = ClassRoom
        fields = [
            'id',
            'class_room_name',
            'teacher',
            'grade_level',
            'subject',
            'period',
            'created_at',
            'duration_class_time',
            'language',
            'm_datetime',
            'r_datetime',
            'removed',
            'video_file_name',
        ]
        read_only_fields = ['id', 'created_at', 'm_datetime', 'r_datetime']
