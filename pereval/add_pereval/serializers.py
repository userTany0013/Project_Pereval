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
    images = ImagesSerializer(many=True)
    class Meta:
        model = Pereval
        fields = ['beauty_title', 'title', 'other_titles', 'connect', 'user', 'status', 'add_time', 'coords', 'level',
                  'images', ]

    def create(self, validated_data):

        user_data = validated_data.pop('user')
        user_instance = User.objects.create(**user_data)
        coords_data = validated_data.pop('coords')
        coords_instance = Coords.objects.create(**coords_data)
        level_data = validated_data.pop('level')
        level_instance = Level.objects.create(**level_data)
        images_data = validated_data.pop('images')
        pereval_instance = Pereval.objects.create(user=user_instance, coords=coords_instance, level=level_instance,
                                                  **validated_data)
        for img in images_data:
            data = img.pop('data')
            title = img.pop('title')
            Images.objects.create(pereval=pereval_instance, data=data, title=title)

        return pereval_instance


class Pereval_InfoSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    images = ImagesSerializer(many=True)
    class Meta:
        model = Pereval
        fields = ['beauty_title', 'title', 'other_titles', 'connect', 'user', 'status', 'add_time', 'coords', 'level',
                  'images', ]


class Coords_UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height', ]

    def update(self, instance, validated_data):
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.height = validated_data.get('height', instance.height)


class Level_UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring', ]

    def update(self, instance, validated_data):
        instance.winter = validated_data.get('winter', instance.winter)
        instance.summer = validated_data.get('summer', instance.summer)
        instance.autumn = validated_data.get('autumn', instance.autumn)
        instance.spring = validated_data.get('spring', instance.spring)



class Images_UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['data', 'title', ]

    def update(self, instance, validated_data):
        instance.data = validated_data.get('data', instance.data)
        instance.title = validated_data.get('title', instance.title)


class Pereval_UpdateSerializer(serializers.ModelSerializer):
    coords = Coords_UpdateSerializer()
    level = Level_UpdateSerializer()
    images = Images_UpdateSerializer(many=True)
    class Meta:
        model = Pereval
        fields = ['beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'status', 'coords', 'level',
                  'images', ]

        def update(self, instance, validated_data):
            instance.beauty_title = validated_data.get('beauty_title', instance.beauty_title)
            instance.title = validated_data.get('title', instance.title)
            instance.other_titles = validated_data.get('other_titles', instance.other_titles)
            instance.connect = validated_data.get('connect', instance.connect)
            instance.status = validated_data.get('status', instance.status)
            coords_data = validated_data.get('coords', instance.coords)
            coords_instance = Coords.objects.create(**coords_data)
            level_data = validated_data.get('level', instance.level)
            level_instance = Coords.objects.create(**level_data)
            images_data = validated_data.get('images', instance.images)
            for img in images_data:
                data = img.pop('data')
                title = img.pop('title')
                Images.objects.create(pereval=instance, data=data, title=title)
