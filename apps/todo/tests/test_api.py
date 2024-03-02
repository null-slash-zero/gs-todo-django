from common.tests import BaseApiTestCase
from django.urls import reverse

class TestTodoAPI(BaseApiTestCase):
  def setUp(self):
    super().setUp()

  def test_get_todo_list(self):
    url = reverse('todo_list-list')

    import ipdb; ipdb.set_trace()
    response = self.client.get(url)

    assert response.status_code == 200
