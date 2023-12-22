from rest_framework.viewsets import ModelViewSet
from .serializers import *

from task.models import Task

class TaskListAPI(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
