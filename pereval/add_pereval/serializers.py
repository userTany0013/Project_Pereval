from django.db import models
from rest_framework import serializers


class Pereval_AddedSerializer(serializers.Serializer):
    date_added = serializers.DateTimeField()
    raw_data = serializers.JSONField()
    images = serializers.JSONField()
    status_id = serializers.ImageField()


class Pereval_ImagesSerializer(serializers.Serializer):
    date_added = serializers.DateTimeField()
    img = serializers.ImageField()
