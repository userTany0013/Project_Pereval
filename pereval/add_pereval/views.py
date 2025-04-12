from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from pereval.add_pereval.models import Pereval_Added, Status, Pereval_Images
from pereval.add_pereval.serializers import Pereval_ImagesSerializer, Pereval_AddedSerializer


# Create your views here.


class submitData(APIView):
    def post(self, request):
        data_new = Pereval_Added.objects.create(
            raw_data=request.data,
            images=request.data['images'],
            status=Status.get(title='new')
        )
        images_new = Pereval_Images.objects.create(
            img=request.data['images']
        )
        return Response({
            'data_new': Pereval_AddedSerializer(data_new).data,
            'images_new': Pereval_ImagesSerializer(images_new).data
        })
