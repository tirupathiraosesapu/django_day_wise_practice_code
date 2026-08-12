from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import ensure_csrf_cookie

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

from .serializers import RegisteredSerializer, LoginSerializer

@api_view(["GET"])
@ensure_csrf_cookie
def csrf_token_view(request):
    return Response({"message": "CSRF cookie set successfully." })


# Create your views here.
class RegisteredAPIView(APIView):
    def post(self, request):
        serializer = RegisteredSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "message": "User registered successfully.",
                    "username": user.username,
                    "email": user.email,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        user = authenticate(username=username, password=password)

        if user is None:
            return Response(
                {"message": "Invalid username or password."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        refresh = RefreshToken.for_user(user)
        access = refresh.access_token
        # login(request, user)

        return Response(
            {
                "message": "Login successful.",
                "username": user.username,
                "access":str(access),
                "refresh":str(refresh)
            },
            status=status.HTTP_200_OK,
        )

class LogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message":"Logout successful." }, status=status.HTTP_200_OK)