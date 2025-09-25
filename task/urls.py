from django.urls import path

from .views import TaskAV, TaskDetailAV

urlpatterns = [
    path('', TaskAV.as_view(), name='task_list_create'),
    path('<int:pk>/', TaskDetailAV.as_view(), name='task_detail'),
]