from rest_framework.routers import DefaultRouter
from apps.todo.api import TodoListViewSet

router = DefaultRouter(trailing_slash=False)

router.register('lists', TodoListViewSet, basename='todo_list')

urlpatterns = router.urls
