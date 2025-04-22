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

from django.http import JsonResponse

from django.contrib.auth.decorators import login_required
import json
#####

import smtplib
import string
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.conf import settings


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
class UserView(APIView):
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



@csrf_exempt
@login_required
def request_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            phone = data.get('phone')

            
            order_id = ''.join(random.choices(string.digits, k=4)) + random.choice(string.ascii_uppercase)

            
            car_details = data.get('car', {})
            car_title = car_details.get('title', 'Unknown Car')
            car_brand = car_details.get('brand', '')
            car_model = car_details.get('model', '')
            car_price = car_details.get('price', '')
            car_description = car_details.get('description', '')

            
            smtp_server = "smtp.yandex.com"
            smtp_port = 587
            smtp_user = "myway.test@yandex.com"
            smtp_password = "ckwsbxbedadgqnyg"  # an application password password from yandex mail

            
            msg1 = MIMEText(f"Your order is accepted.\nA sales manager will contact you soon.\n\nOrder ID: {order_id}")
            msg1['Subject'] = "Order Confirmation"
            msg1['From'] = f"No Reply <{smtp_user}>"
            msg1['To'] = email

            
            admin_body = f"""
New order received:

Name: {name}
Email: {email}
Phone: {phone}

Car Details:
Title: {car_title}
Brand: {car_brand}
Model: {car_model}
Price: ${car_price}
Description: {car_description}

Order ID: {order_id}
"""
            msg2 = MIMEText(admin_body)
            msg2['Subject'] = f"New Order - {order_id}"
            msg2['From'] = f"No Reply <{smtp_user}>"
            msg2['To'] = "mywayshowroom3@gmail.com"

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_user, smtp_password)
                server.sendmail(smtp_user, email, msg1.as_string())
                server.sendmail(smtp_user, "mywayshowroom3@gmail.com", msg2.as_string())

            return JsonResponse({
                'status': 'success',
                'order_id': order_id,
                'message': 'Order received and emails sent'
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
