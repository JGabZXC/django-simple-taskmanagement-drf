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

    def to_internal_value(self, data):
        status_map = {
            'pending': 1,
            'in_progress': 2,
            'done': 3,
        }
        if data not in status_map:
            raise serializers.ValidationError(f"Invalid status: {data}")
        return status_map[data]

class TaskSerializer(serializers.ModelSerializer):
    status = StatusField()

    class Meta:
        model = Task
        fields = '__all__'

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")

        return value