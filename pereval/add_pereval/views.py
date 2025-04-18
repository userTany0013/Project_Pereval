from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Pereval, User
from .serializers import Pereval_AddedSerializer


# Create your views here.


class submitData(APIView):
    def post(self, request):
        data_new = Pereval.objects.create(
            beauty_title=request.data["beauty_title"],
            title=request.data["title"],
            other_titles=request.data["other_titles"],
            connect=request.data["connect"],
            user=User.objects.get(email=request.data["user"]["email"]),
            status='NE'

        )
        return Response({
            'data_new': Pereval_AddedSerializer(data_new).data,
        })
