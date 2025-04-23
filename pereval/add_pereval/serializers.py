from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'fam', 'name', 'otc', 'phone', ]


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height', ]


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring', ]


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['data', 'title', ]


class Pereval_AddedSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    images = ImagesSerializer()
    class Meta:
        model = Pereval
        fields = ['beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'user', 'status', 'coords', 'level',
                  'images', ]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_instance = User.objects.create(**user_data)
        coords_data = validated_data.pop('coords')
        coords_instance = Coords.objects.create(**coords_data)
        level_data = validated_data.pop('level')
        level_instance = Coords.objects.create(**level_data)
        images_data = validated_data.pop('images')
        pereval_instance = Pereval.objects.create(user=user_instance, coords=coords_instance, level=level_instance,
                                                  **validated_data)
        for img in images_data:
            data = img.pop('data')
            title = img.pop('title')
            Images.objects.create(pereval=pereval_instance, data=data, title=title)

        return pereval_instance


class Pereval_InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval
        fields = ['beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'user', 'status', ]

