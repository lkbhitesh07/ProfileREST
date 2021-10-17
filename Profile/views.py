from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status
from .serializers import ProfileSerializer, RestrictedSerializer
from .models import Profile

# All the views

class ProfileView(APIView):
    serializer_class = ProfileSerializer

    def get(self, request, format=None):
        profile_data = Profile.objects.all()
        serializer = self.serializer_class(profile_data, many=True)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

class OnlyPausedProfileView(APIView):
    serializer_class = ProfileSerializer

    def get(self, request, format=None):
        profile_data = Profile.objects.filter(status__iexact="PAUSED")
        serializer = self.serializer_class(profile_data, many=True)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

class PauseAProfileView(APIView):
    serializer_class = RestrictedSerializer

    # def get(self, request, name, format=None):
    #     profile = Profile.objects.get(name__iexact=name)

    #     serializer = self.serializer_class(profile, data = {'status':'PAUSED'})
    #     if serializer.is_valid():
    #         serializer.save()
    #         serialized_data = serializer.data
    #         return Response(serialized_data, status=status.HTTP_200_OK)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, name, format=None):
        profile = Profile.objects.get(name__iexact=name)
        serializer = self.serializer_class(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UnpauseAProfileView(APIView):
    serializer_class = ProfileSerializer

    def get(self, request, name, format=None):
        profile = Profile.objects.get(name__iexact=name)

        if profile.status == "PAUSED":
            profile.status = "ACTIVE"
            profile.save()
        else:
            pass

        serializer = self.serializer_class(profile)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

class CreateProfileView(APIView):
    serializer_class = ProfileSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteProfileView(APIView):

    def delete(self, request, name, format=None):
        profile = Profile.objects.get(name__iexact=name)
        profile.delete()
        return Response(status=status.HTTP_200_OK)
