from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register('', TaskViewSet)

app_name = 'task'

urlpatterns = [
    path(r'task-list', include(router.urls), name='task-list'),
    path(r'task-create', TaskViewSet.as_view({'post': 'create'}), name='task-create'),
    path(r'<int:pk>', TaskViewSet.as_view({'get': 'retrieve'}), name='task-detail'),
]
