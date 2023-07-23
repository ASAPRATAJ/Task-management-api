from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

app_name = 'task'

urlpatterns = [
    path('api/task/task-list/', include(router.urls), name='task-list'),
    path('api/task/task-create/', TaskViewSet.as_view({'post': 'create'}), name='task-create'),
]
