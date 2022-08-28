from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from users.serializers import UserSerializer


class AuthenticationView(ViewSet):
    @action(detail=False, methods=['post'], url_path="create-account", name='create-account')
    def create_account(self, request):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        password = request.data.get('password')

        if not first_name or not last_name or not email or not password:
            return Response({"detail": "Bad request"}, status=400)

        usr = User.objects.filter(email=request.data.get("email")).first()
        if usr:
            return Response({"detail": "Account with this email already exists"}, status=409)

        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=email,
            is_active=True
        )

        user.save()
        user.set_password(password)
        user.save()

        context = {
            "request": request
        }

        data = UserSerializer(user, context=context).data

        token, _ = Token.objects.get_or_create(
            user=user
        )
        data["token"] = token.key
        data['detail'] = 'Your account has been created. Verify your email to continue'

        return Response(data, status=201)

    @action(detail=False, methods=['post'], url_path='login', url_name='login')
    def sign_in(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password, request=request)

        if not user:
            return Response({"detail": "Invalid credentials"}, status=400)

        login(request=request, user=user)

        context = {
            "request": request
        }

        data = UserSerializer(user, context=context).data

        token, _ = Token.objects.get_or_create(
            user=user
        )
        data["token"] = token.key
        return Response(data, status=200)

    @action(detail=False, methods=['get'], url_path="logout", name='logout')
    def sign_out(self, request):
        if request.user.is_anonymous:
            return Response({"detail": "You are not allowed to perform this operation"}, status=403)
        Token.objects.filter(user=request.user).delete()
        logout(request)
        return Response({"detail": "Signed out"}, status=200)

