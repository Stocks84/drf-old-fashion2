from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Game

class GameTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.game = Game.objects.create(title="Test Game", description="Test Description", creator=self.user)

    def test_list_games(self):
        response = self.client.get('/api/games/games/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_game(self):
        data = {"title": "New Game", "description": "New Description"}
        response = self.client.post('/api/games/games/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_game(self):
        response = self.client.get(f'/api/games/games/{self.game.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_game(self):
        data = {"title": "Updated Game", "description": "Updated Description"}
        response = self.client.put(f'/api/games/games/{self.game.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_game(self):
        response = self.client.delete(f'/api/games/games/{self.game.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
