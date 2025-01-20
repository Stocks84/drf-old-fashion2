from django.urls import path
from .views import UserProfileListCreateView, UserProfileDetailView, UserDetailView

urlpatterns = [
    path('', UserProfileListCreateView.as_view(), name='profile-list-create'),
    path('<int:pk>/', UserProfileDetailView.as_view(), name='profile-detail'),
    path('<int:user_id>/', UserDetailView.as_view(), name='user-detail'),  # **NEW**
]
