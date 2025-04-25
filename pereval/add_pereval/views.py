from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Pereval, User, Images
from .serializers import Pereval_Serializer, Pereval_InfoSerializer, Pereval_UpdateSerializer


# Create your views here.


class submitData(APIView):
    queryset = Pereval.objects.all()
    serializer_class = Pereval_Serializer
    filterset_fields = ('user__email',)

    def post(self, request):
        serializer = Pereval_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'status': 'error', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        obj = Pereval.objects.get(id=pk)
        return Response(Pereval_InfoSerializer(obj).data)

    def patch(self, request, pk):
        pereval_obj = Pereval.objects.get(id=pk)
        serializer = Pereval_UpdateSerializer(pereval_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response()
        return Response()
