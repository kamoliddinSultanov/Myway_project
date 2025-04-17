from rest_framework import viewsets
from .models import Car
from .serializers import CarSerializer

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from elasticsearch import Elasticsearch


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated


from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from .auth import CustomSessionAuthentication

from django.middleware.csrf import get_token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import JsonResponse



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json

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

####
@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        return Response({"detail": "CSRF cookie set"})


@method_decorator(ensure_csrf_cookie, name='dispatch')
class UserView(APIView):  # Добавляем обратно UserView
    authentication_classes = [CustomSessionAuthentication]

    def get(self, request):
        if request.user.is_authenticated:
            return Response({
                'username': request.user.username,
                'email': request.user.email
            })
        return Response(
            {"error": "Not authenticated"},
            status=status.HTTP_401_UNAUTHORIZED
        )



@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(APIView):
    authentication_classes = [CustomSessionAuthentication]
    permission_classes = []

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
                if user:
                    return Response(
                        {"message": "User created successfully"},
                        status=status.HTTP_201_CREATED
                    )
            except Exception as e:
                return Response(
                    {"error": str(e)},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    authentication_classes = [CustomSessionAuthentication]
    permission_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response(
                {"error": "Please provide both username and password"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return Response({
                "username": user.username,
                "email": user.email
            })
        return Response(
            {"error": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED
        )


@method_decorator(ensure_csrf_cookie, name='dispatch')
class LogoutView(APIView):
    authentication_classes = [CustomSessionAuthentication]

    def post(self, request):
        logout(request)
        return Response({"message": "Successfully logged out"})



@api_view(['GET'])
def get_csrf_token(request):
    """
    Возвращает CSRF токен для фронтенда.
    """
    csrf_token = get_token(request)
    return Response({'csrfToken': csrf_token})


@login_required
def check_auth(request):
    return JsonResponse({'isAuthenticated': True})

@csrf_exempt  # Временно отключаем CSRF для тестирования
@login_required
def request_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Здесь можно добавить обработку данных заказа
            # Например, сохранение в базу данных
            return JsonResponse({
                'status': 'success',
                'message': 'Order received successfully'
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    return JsonResponse({
        'status': 'error',
        'message': 'Only POST requests allowed'
    }, status=405)