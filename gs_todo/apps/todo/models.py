from django.db import models
from common.mixins import TimeStampedModelMixin

class TodoList(TimeStampedModelMixin):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class TodoItem(TimeStampedModelMixin):
    description = models.TextField()
    completed = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def __str__(self):
        return self.description