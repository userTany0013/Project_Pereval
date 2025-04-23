from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Pereval, User, Images
from .serializers import Pereval_AddedSerializer, Pereval_InfoSerializer


# Create your views here.


class submitData(APIView):
    def post(self, request):
        Pereval_AddedSerializer.create(self, validated_data=request)
        return Response({
            '': ''
        })

    def GET(self, request):
        pereval_info = Pereval.objects.get(id=request.data['id'])
        return Response({
            'pereval_info': Pereval_InfoSerializer(pereval_info).data
        })

#    def PATCH(self, request):
