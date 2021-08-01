
from django.db.models import fields
from rest_framework import serializers
from .models import User, UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['id', 'userName', 'password', 'role']
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    userName = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=20)

    def getUserName(self):
        return self.userName

    def getPassword(self):
        return self.password
