from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from rest_framework.response import Response
from rest_framework import status 
from .serializers import UserSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.

class UserGetCreate(APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve all users",
        operation_description="Returns a list of all users stored in the database.",
        responses={200: UserSerializer(many=True)}
    )
    def get(self,request):
        users = User.objects.all()
        if not users:
            return Response({"error":"No users foung"},status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        operation_summary="Create a new user",
        operation_description="Creates a new user with a unique email.",
        request_body=UserSerializer,
        responses={
            201: UserSerializer,
            400: openapi.Response("Validation errors", UserSerializer)
        }
    )
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({"error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)