from django.urls import path
from .views import GameListCreateView, GameDetailView, LikeCreateView, CommentListCreateView, GameRecentView

urlpatterns = [
    path('', GameListCreateView.as_view(), name='game-list-create'),
    path('<int:pk>/', GameDetailView.as_view(), name='game-detail'),
    path('<int:pk>/like/', LikeCreateView.as_view(), name='game-like'),
    path('<int:pk>/comments/', CommentListCreateView.as_view(), name='game-comments'),
    path('recent/', GameRecentView.as_view(), name='game-recent'),
    path('<int:game_id>/comments/', CommentListCreateView.as_view(), name='game-comments'),
]