from django.test import TestCase

from apps.todo.serializers import TodoItemSerializer, TodoListSerializer
from apps.todo.models import TodoItem, TodoList

class TodoListSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.todo_list = TodoList.objects.create(
            name='Test Todo List',
            description='Test Todo List Description'
        )
        cls.todo_item = TodoItem.objects.create(
            description='Test Todo Item',
            completed=False,
            todo_list=cls.todo_list
        )


    def test_serializer_fields(self):
        serializer = TodoListSerializer(self.todo_list)
        data = serializer.data

        assert set(data.keys()) == set(['name', 'description'])

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

        assert data['description'] == 'Test Todo Item'
        assert data['completed'] == False
