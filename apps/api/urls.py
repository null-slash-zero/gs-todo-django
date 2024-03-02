from django.conf.urls import include
from django.urls import re_path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
urlpatterns = router.urls

urlpatterns += [re_path('^todo/', include('apps.todo.urls'))]
