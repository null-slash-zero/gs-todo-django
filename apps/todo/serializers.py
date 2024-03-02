from rest_framework import serializers

from apps.todo.models import TodoList, TodoItem

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('description', 'completed')
class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('name', 'description')

