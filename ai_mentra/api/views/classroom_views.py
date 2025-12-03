from rest_framework import viewsets
from api.models.classroom import ClassRoom
from api.serializers.classroom_serializer import ClassRoomSerializer


class ClassRoomViewSet(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer