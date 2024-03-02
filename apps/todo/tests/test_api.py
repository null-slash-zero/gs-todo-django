from common.tests import BaseApiTestCase
from django.urls import reverse

from apps.todo.models import TodoItem, TodoList

class TestTodoListAPI(BaseApiTestCase):
  @classmethod
  def setUpTestData(cls):
    super().setUpTestData()
    cls.todo_list = TodoList.objects.create(name='Test Todo List', description='Test Description')
    cls.todo_items = [
      TodoItem.objects.create(description='Test Todo Item 1', todo_list=cls.todo_list),
      TodoItem.objects.create(description='Test Todo Item 2', todo_list=cls.todo_list),
      TodoItem.objects.create(description='Test Todo Item 3', todo_list=cls.todo_list),
    ]

  @classmethod
  def tearDownClass(cls):
    super().tearDownClass()
    cls.todo_list.delete()

  def test_get_todo_lists(self):
    url = reverse('todo_list-list')

    response = self.client.get(url)
    data = response.json()

    assert response.status_code == 200

    assert len(data) == 1
    assert data[0]['id'] == self.todo_list.id
    assert data[0]['name'] == self.todo_list.name
    assert data[0]['description'] == self.todo_list.description

  def test_get_todo_list_detail(self):
    url = reverse('todo_list-detail', kwargs={'pk': self.todo_list.id})

    response = self.client.get(url)
    data = response.json()

    assert response.status_code == 200

    assert data['id'] == self.todo_list.id
    assert data['name'] == self.todo_list.name
    assert data['description'] == self.todo_list.description

    for i, item in enumerate(data['items']):
      assert item['id'] == self.todo_items[i].id
      assert item['description'] == self.todo_items[i].description
      assert item['completed'] == self.todo_items[i].completed
