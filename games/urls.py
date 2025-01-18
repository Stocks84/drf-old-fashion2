from django.urls import path
from .views import GameListCreateView, GameDetailView, LikeCreateView, CommentListCreateView

urlpatterns = [
    path('games/', GameListCreateView.as_view(), name='game-list-create'),
    path('games/<int:pk>/', GameDetailView.as_view(), name='game-detail'),
    path('games/<int:pk>/like/', LikeCreateView.as_view(), name='game-like'),
    path('games/<int:pk>/comments/', CommentListCreateView.as_view(), name='game-comments'),
    path('games/recent/', GameRecentView.as_view(), name='game-recent'),
]