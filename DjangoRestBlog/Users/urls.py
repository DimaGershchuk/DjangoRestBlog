
from django.urls import path
from .views import UserDetailView,UserListView

urlpatterns = [
    path('users-list/', UserListView.as_view(), name='user-list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]