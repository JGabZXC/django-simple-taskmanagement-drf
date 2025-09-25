from django.urls import path
from .views import ProjectAV, ProjectDetailAV

urlpatterns = [
    path('', ProjectAV.as_view(), name='project_list_create'),
    path('<int:pk>/', ProjectDetailAV.as_view(), name='project_detail'),
]