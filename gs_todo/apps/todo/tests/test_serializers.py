from django.test import TestCase

from apps.todo.serializers import TodoItemSerializer
from apps.todo.models import TodoItem, TodoList


class TodoItemSerializerTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.todo_list = TodoList.objects.create(
            name='Test Todo List',
            description='Test Todo List Description'
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        TodoList.objects.all().delete()

    def test_todo_item_serializer(self):
        todo_item = TodoItem.objects.create(
            description='Test Todo Item',
            completed=False,
            todo_list=self.todo_list
        )
        serializer = TodoItemSerializer(todo_item)
        data = serializer.data

        assert data['id'] == todo_item.id
        assert data['description'] == 'Test Todo Item'
        assert data['completed'] == False
        assert data['todo_list'] == self.todo_list.id
        assert data['created_at'] == todo_item.created_at.strftime('%Y-%m-%d %H:%M:%S')
        assert data['updated_at'] == todo_item.updated_at.strftime('%Y-%m-%d %H:%M:%S')
