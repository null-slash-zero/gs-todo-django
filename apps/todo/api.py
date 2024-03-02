from rest_framework import viewsets;

from apps.todo.models import TodoList;
from apps.todo.serializers import TodoListSerializer, TodoListDetailSerializer;

class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return self.serializer_class

        return TodoListDetailSerializer