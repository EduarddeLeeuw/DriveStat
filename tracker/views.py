from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Vehicle
from .serializers import VehicleSerializer

# Create your views here.
@api_view(['GET'])
def rest_get_vehicle(request, vehicle_id):
    try:
        vehicle = Vehicle.objects.get(pk=vehicle_id)
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)
    except Vehicle.DoesNotExist:
        return Response({'error': 'Vehicle not found.'}, status=status.HTTP_404_NOT_FOUND)