from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet

from . import views

from .views import search_cars

from . import auth

from .views import get_csrf_token

from . import views

router = DefaultRouter()
router.register(r'cars', CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search/', search_cars, name='search_cars'),
    path('api/csrf-token/', get_csrf_token, name='csrf_token'),
    path('authenticated/', views.check_auth),
    path('request-order/', views.request_order),
    path('cars/<int:pk>/', views.car_detail, name='car_detail'),
]