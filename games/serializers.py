from rest_framework import serializers
from .models import Game, Like, Comment

class GameSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Game
        fields = ['id', 'title', 'description', 'creator', 'created_at', 'updated_at']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'game', 'user']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'game', 'user', 'text', 'created_at']
