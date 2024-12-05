from rest_framework.serializers import ModelSerializer
from subtask_app.serializers import SubtaskSerializer
from .models import Task

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    
class DetailedTaskSerializer(ModelSerializer):
    subtasks = SubtaskSerializer(many=True)
    class Meta:
        model = Task
        fields = '__all__'

"""
TaskSerializer
{
 'title':'something',
 'is_completed': False,
}

DetailedTaskSerializer
{
 'title':'something',
 'is_completed': False,
 'subtasks':[
  {}, {}, {}
 ]
}
"""