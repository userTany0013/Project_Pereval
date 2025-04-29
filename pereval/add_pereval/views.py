from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Pereval, User, Images
from .serializers import Pereval_Serializer, Pereval_InfoSerializer, Pereval_UpdateSerializer


# Create your views here.


class submitData(APIView):

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


class submitData_filter(APIView):
    def get(self, request):
        queryset = Pereval.objects.all()
        user__email = request.query_params.get('user__email')
        if user__email:
            queryset = queryset.filter(user__email=user__email)
            serializer = Pereval_Serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
