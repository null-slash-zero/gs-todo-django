from rest_framework import viewsets;

from apps.todo.models import TodoList;
from apps.todo.serializers import TodoListSerializer;

class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer