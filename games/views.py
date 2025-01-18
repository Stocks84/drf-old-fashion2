from rest_framework.views import APIView
from rest_framework import generics, permissions
from .models import Game, Like, Comment
from .serializers import GameSerializer, LikeSerializer, CommentSerializer

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
    def get(self, request):
        recent_games = Game.objects.order_by('-created_at')[:5]
        serializer = GameSerializer(recent_games, many=True)
        return Response(serializer.data)
