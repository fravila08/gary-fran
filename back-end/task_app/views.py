from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404
from .serializers import TaskSerializer, Task

# Create your views here.
class AllTasks(APIView):
  def get(self, request):
    tasks = Task.objects.all()
    return Response(TaskSerializer(tasks, many=True).data)
    
  def post(self, request):
    # grab data from the request
    data = request.data
    # we want to utilize the serializer to attempt to create data
    serializedtask = TaskSerializer(data=data) #{title}
    # validate data
    if serializedtask.is_valid():
      # if valid save and respond
      serializedtask.save()
      return Response(serializedtask.data, status=HTTP_201_CREATED)
    # respond with user errors
    return Response(serializedtask.errors, status=HTTP_400_BAD_REQUEST)

class ATask(APIView):
  def get(self, request, task_id):
    pass

  def put(self, request, task_id):
    pass

  def delete(self, request, task_id):
    pass