from rest_framework import serializers


class Pereval_AddedSerializer(serializers.Serializer):
    beauty_title = serializers.CharField()
    title = serializers.CharField()
    other_titles = serializers.CharField()
    connect = serializers.CharField()



class Pereval_InfoSerializer(serializers.Serializer):
    beauty_title = serializers.CharField()
    title = serializers.CharField()
    other_titles = serializers.CharField()
    connect = serializers.CharField()
    add_time = serializers.DateTimeField()
    user = serializers.EmailField()
    status = serializers.CharField()
