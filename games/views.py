from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Game, Like, Comment
from .serializers import GameSerializer, LikeSerializer, CommentSerializer
from rest_framework.exceptions import NotFound

class GameListCreateView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class GameDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Game.objects.filter(creator=self.request.user)

class LikeCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        game_id = self.kwargs.get("game_id")
        try:
            game = Game.objects.get(pk=game_id)
        except Game.DoesNotExist:
            raise NotFound("Game not found")
        return game.comments.all()  # Fetch comments for this game

    def perform_create(self, serializer):
        game_id = self.kwargs.get("game_id")
        try:
            game = Game.objects.get(pk=game_id)
        except Game.DoesNotExist:
            raise NotFound("Game not found")
        serializer.save(user=self.request.user, game=game)

class GameRecentView(APIView):
    """
    View to list the most recent games.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            recent_games = Game.objects.order_by('-created_at')[:10]  # Fetch recent games
            serializer = GameSerializer(recent_games, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)  # Return error details