from rest_framework import viewsets
from .models import Car
from .serializers import CarSerializer

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    car_data = {
        "title": car.title,
        "brand": car.brand,
        "model": car.model,
        "price": car.price,
        "description": car.description,
        "image": car.image.url,
    }
    return JsonResponse(car_data)