from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

class UserProfileTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_create_profile(self):
        data = {"age": 25, "location": "New York", "favorite_drink": "Mojito"}
        response = self.client.post('/api/users/profiles/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_profiles(self):
        response = self.client.get('/api/users/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_profile(self):
        response = self.client.get(f'/api/users/profiles/{self.user.profile.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_profile(self):
        data = {"age": 30, "location": "Los Angeles", "favorite_drink": "Whiskey Sour"}
        response = self.client.put(f'/api/users/profiles/{self.user.profile.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_profile(self):
        response = self.client.delete(f'/api/users/profiles/{self.user.profile.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
