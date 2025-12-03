# serializers/user_serializer.py
from rest_framework import serializers
from api.models.user import UserProfile

class UserSerializer(serializers.ModelSerializer):
    # Make password write-only
    user_password = serializers.CharField(write_only=True, required=True, min_length=8)
    
    class Meta:
        model = UserProfile
        fields = [
            'id',
            'user_email',
            'user_name',
            'user_school',
            'profile_picture_url',
            'user_password',
            'enabled',
            'removed',
            'admin',
            'temp_password',
            'm_datetime',
            'r_datetime',
            'is_staff',
            'is_active',
        ]
        read_only_fields = ['id', 'm_datetime', 'r_datetime', 'is_staff', 'is_active']

    def create(self, validated_data):
        password = validated_data.pop('user_password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('user_password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
