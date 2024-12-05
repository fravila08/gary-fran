from django.urls import path
from .views import AllTasks, ATask

urlpatterns = [
  path("", AllTasks.as_view())
]


#   path("api/v1/tasks/",include("task_app.urls"))
