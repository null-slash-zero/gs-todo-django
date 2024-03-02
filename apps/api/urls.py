from django.conf.urls import include
from django.urls import re_path
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
urlpatterns = router.urls

urlpatterns += [re_path(r'^todo', include('apps.todo.urls'))]
