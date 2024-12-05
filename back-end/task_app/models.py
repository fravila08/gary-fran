from django.db import models

# Create your models here.
# task: title, completed

class Task(models.Model):
    title = models.CharField(max_length=50)
    is_completed = models.BooleanField(default=False)
    # subtasks = [subtask, subtask, subtask]