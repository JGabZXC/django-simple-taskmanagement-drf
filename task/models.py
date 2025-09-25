from django.db import models

from project.models import Project

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = (
        (1, 'Pending'),
        (2, 'In Progress'),
        (3, 'Done'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.IntegerField(default=1, choices=STATUS_CHOICES)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title