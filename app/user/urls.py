from django.urls import path, include
from .views import CreateUserView, ListUserView

app_name = 'user'

urlpatterns = [
    path('create', CreateUserView.as_view(), name='create'),
    path('list', ListUserView.as_view(), name='list'),
]