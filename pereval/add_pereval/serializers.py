from rest_framework import serializers


class Pereval_AddedSerializer(serializers.Serializer):
    beauty_title = serializers.CharField()
    title = serializers.CharField()
    other_titles = serializers.CharField()
    connect = serializers.CharField()
    user = serializers.EmailField()




#    date_added = serializers.DateTimeField()
#    raw_data = serializers.JSONField()
#    images = serializers.JSONField()
#    status_id = serializers.ImageField()
