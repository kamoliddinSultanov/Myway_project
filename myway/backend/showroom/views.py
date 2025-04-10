from rest_framework import viewsets
from .models import Car
from .serializers import CarSerializer

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from elasticsearch import Elasticsearch

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
        #"image": car.image.url,
        "image": request.build_absolute_uri(car.image.url) if car.image else None,
    }
    return JsonResponse(car_data)


es = Elasticsearch(hosts=["http://localhost:9200"])


def search_cars(request):
    query = request.GET.get('q', '').strip()
    if not query:
        return JsonResponse({"error": "empty request"}, status=400)

    try:
        response = es.search(
            index="cars",
            body={
                "query": {
                    "multi_match": {
                        "query": query,
                        "fields": ["title^3", "brand^2", "model", "description"],
                        "fuzziness": "AUTO"
                    }
                }
            }
        )
        hits = response["hits"]["hits"]
        cars = [hit["_source"] for hit in hits]
        return JsonResponse(cars, safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

# В файле views.py добавьте функцию
def index_all_cars():
    for car in Car.objects.all():
        doc = {
            "id": car.id,
            "title": car.title,
            "brand": car.brand,
            "model": car.model,
            "price": float(car.price),
            "description": car.description,
            "image": car.image.url if car.image else None
        }
        es.index(index="cars", id=car.id, document=doc)
    return "all cars are indexed"
