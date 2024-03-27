from django.urls import path

from rest_framework.routers import DefaultRouter

from apps.todo.api import TodoListViewSet, TodoListItemsViewSet

router = DefaultRouter(trailing_slash=False)

router.register('lists', TodoListViewSet, basename='todo_list')

urlpatterns = router.urls

urlpatterns += [
    path('lists/<int:list_pk>/items', TodoListItemsViewSet.as_view({'get': 'list', 'post': 'create'}), name='todo_list_item-list'),
    path('lists/<int:list_pk>/items/<int:pk>', TodoListItemsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='todo_list_item-detail'),
]