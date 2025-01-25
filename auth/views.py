from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserLoginSerializer, UserSignupSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
            # Ensure that the response contains the correct token data
            access_token = response.data.get('access')
            refresh_token = response.data.get('refresh')

            if not access_token or not refresh_token:
                return Response({'detail': 'Tokens not generated'}, status=status.HTTP_400_BAD_REQUEST)

            return Response({
                'access': access_token,
                'refresh': refresh_token
            }, status=status.HTTP_200_OK)

        return response




class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Logout successful."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"detail": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)

class SignupView(APIView):
    permission_classes = [AllowAny]  # Allow unauthenticated access

    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "User created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


