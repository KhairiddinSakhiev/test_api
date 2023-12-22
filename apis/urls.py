from rest_framework.routers import SimpleRouter
from django.urls import path, include
from .views import *

router = SimpleRouter()

router.register(r'', TaskListAPI)

urlpatterns = [
    path('', include(router.urls))
]




# from django.urls import path
# from .views import TaskListAPIView

# urlpatterns = [
#     path('', TaskListAPIView.as_view(), name="task_api_view"),
# ]
