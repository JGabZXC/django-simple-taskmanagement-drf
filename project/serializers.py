from rest_framework import serializers

from task.serializers import TaskSerializer
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'

    def validate_name(self, value):
        print("Validating name:", value)
        if len(value) < 3:
            raise serializers.ValidationError('Name must be at least 3 characters long')

        return value