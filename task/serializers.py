from rest_framework import serializers

from project.models import Project
from .models import Task

class StatusField(serializers.Field):
    def to_representation(self, value):
        status_map = {
            1: 'Pending',
            2: 'In Progress',
            3: 'Done',
        }
        return status_map.get(value, 'Unknown')

class TaskSerializer(serializers.ModelSerializer):
    status = StatusField()

    class Meta:
        model = Task
        fields = '__all__'

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")

        return value