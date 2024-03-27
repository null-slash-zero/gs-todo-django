from rest_framework import viewsets;
from rest_framework.renderers import JSONRenderer;
from rest_framework.response import Response;

from apps.todo.models import TodoList, TodoItem;
from apps.todo.serializers import TodoListSerializer, TodoListDetailSerializer, TodoItemSerializer;

class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    renderer_classes = [JSONRenderer]

    def get_serializer_class(self):
        if self.action == 'list':
            return self.serializer_class

        return TodoListDetailSerializer

class TodoListItemsViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoItemSerializer
    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        return TodoItem.objects.filter(todo_list=self.kwargs['list_pk'])

    def create(self, request, list_pk):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(todo_list_id=list_pk)
        return Response(serializer.data)

    def update(self, request, list_pk, pk):
        try:
            todo_item = TodoItem.objects.get(pk=pk, todo_list=list_pk)
        except TodoItem.DoesNotExist:
            return Response(status=404)

        serializer = self.get_serializer(todo_item, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, list_pk, pk):
        try:
            todo_item = TodoItem.objects.get(pk=pk, todo_list=list_pk)
        except TodoItem.DoesNotExist:
            return Response(status=404)

        todo_item.delete()
        return Response(status=204)