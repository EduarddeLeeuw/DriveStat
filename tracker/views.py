from django.shortcuts import render
from rest_framework import status, permissions, renderers
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from .models import Vehicle
from .serializers import VehicleSerializer

# Create your views here.
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def rest_get_vehicle(request, vehicle_id):
    try:
        vehicle = Vehicle.objects.get(pk=vehicle_id)
        if vehicle.owner != request.user:
                    return Response({'error': 'You do not have permission to view this vehicle!'}, status=status.HTTP_403_FORBIDDEN)
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)
    except Vehicle.DoesNotExist:
        return Response({'error': 'Vehicle not found.'}, status=status.HTTP_404_NOT_FOUND)