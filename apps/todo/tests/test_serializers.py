from django.test import TestCase
from django.utils import timezone

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

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        TodoList.objects.all().delete()


    def test_serializer_fields(self):
        serializer = TodoListSerializer(self.todo_list)
        data = serializer.data

        assert set(data.keys()) == set(['name', 'description', 'created_at', 'updated_at'])

    def test_serializer_data(self):
        serializer = TodoListSerializer(self.todo_list)
        data = serializer.data

        assert data['name'] == self.todo_list.name
        assert data['description'] == self.todo_list.description

class TodoItemSerializerTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.todo_list = TodoList.objects.create(
            name='Test Todo List',
            description='Test Todo List Description'
        )
        cls.todo_item = TodoItem.objects.create(
            description='Test Todo Item',
            completed=False,
            todo_list=cls.todo_list
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        TodoList.objects.all().delete()

    def test_serializer_fields(self):
        serializer = TodoItemSerializer(self.todo_item)
        data = serializer.data

        assert set(data.keys()) == set(['description', 'completed', 'created_at', 'updated_at'])

    def test_serializer_data(self):
        serializer = TodoItemSerializer(self.todo_item)
        data = serializer.data

        assert data['description'] == self.todo_item.description
        assert data['completed'] == self.todo_item.completed
