# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.classroom_views import ClassRoomViewSet
from api.views.user_views import UserViewSet

router = DefaultRouter()
router.register(r'classrooms', ClassRoomViewSet, basename='classroom')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
