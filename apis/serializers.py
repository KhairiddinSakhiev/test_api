from rest_framework import serializers
from django.contrib.auth.models import User

from task.models import Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
        

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = '__all__'
        
        