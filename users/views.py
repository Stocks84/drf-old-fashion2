from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserProfileSerializer

# List and Create Profiles
class UserProfileListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

# Retrieve, Update, Delete Profiles
class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Ensure only the profile owner can update/delete
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
