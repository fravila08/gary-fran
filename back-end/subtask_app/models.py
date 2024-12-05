from django.db import models
from task_app.models import Task
# Create your models here.
# subtask = many subtasks -> 1 task, title, completed, description
# foreignkey, onetoone, manytomany

class Subtask(models.Model):
    title = models.CharField(max_length=50)
    is_completed = models.BooleanField(default=False)
    description = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')