from rest_framework import serializers

from apps.todo.models import TodoList, TodoItem

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('id', 'description', 'completed', 'created_at', 'updated_at')
class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')

class TodoListDetailSerializer(TodoListSerializer):
    items = TodoItemSerializer(many=True, read_only=True)

    class Meta(TodoListSerializer.Meta):
        fields = TodoListSerializer.Meta.fields + ('items',)
