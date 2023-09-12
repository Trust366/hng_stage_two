from django.contrib.auth.models import User
from rest_framework import serializers
from .models import CustomUser

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['name']
        
        def create(self, validated_data):
            
            user = CustomUser.objects.create(**validated_data)
            user.save()
            
            
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','name']
        
       
        
        