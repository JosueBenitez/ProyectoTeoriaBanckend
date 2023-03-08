from django.http.response import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Temperatura
from .serializers import TemperaturaSerializer
from rest_framework.response import Response

class TemperaturaAPIView(APIView):

    # READ a single Temperatura
    def get_object(self, pk):
        try:
            return Temperatura.objects.get(pk=pk)
        except Temperatura.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
        else:
            data = Temperatura.objects.all()

        serializer = TemperaturaSerializer(data, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = TemperaturaSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Temperatura Created Successfully',
            'data': serializer.data
        }

        return response

    def put(self, request, pk=None, format=None):
        temperatura_to_update = Temperatura.objects.get(pk=pk)
        serializer = TemperaturaSerializer(instance=temperatura_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Temperatura Updated Successfully',
            'data': serializer.data
        }

        return response

    def delete(self, request, pk, format=None):
        temperatura_to_delete =  Temperatura.objects.get(pk=pk)

        temperatura_to_delete.delete()

        return Response({
            'message': 'Temperatura Deleted Successfully'
        })
