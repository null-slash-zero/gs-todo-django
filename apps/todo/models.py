from django.db import models
from common.mixins import TimeStampedModelMixin

class TodoList(TimeStampedModelMixin):
    """
    Model representing a Todo List
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class TodoItem(TimeStampedModelMixin):
    """
    Model representing a Todo Item
    """
    description = models.TextField()
    completed = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.description