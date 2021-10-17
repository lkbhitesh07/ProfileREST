from django.db.models import fields
from .models import Profile
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'name',
            'dob',
            'status'
        ]

class RestrictedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'status'
        ]