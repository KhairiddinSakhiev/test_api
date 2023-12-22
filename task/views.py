from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from rest_framework import permissions

from .permissions import MyPermissions
from .models import Task

# Create your views here.

class TaskListView(ListView):
    model = Task
    permission_classes = [permissions.IsAuthenticated]
    template_name = "tasks_list.html"

class TasksCreateView(CreateView):
    model = Task
    template_name = "create.html"
    fields = ['title', 'user', 'due_date', 'is_done']
    success_url = reverse_lazy("task_list")
    
class TaskUpdateView(UpdateView):
    model = Task
    template_name = "update.html"
    fields = ['title', 'user', 'due_date', 'is_done']
    success_url = reverse_lazy("task_list")
    
class TaskDetailView(DetailView):
    model = Task
    template_name = "task_detail.html"
    
class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task_delete.html"
    success_url = reverse_lazy("task_list")
    




