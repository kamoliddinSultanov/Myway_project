from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet

from . import views

router = DefaultRouter()
router.register(r'cars', CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cars/<int:pk>/', views.car_detail, name='car_detail'),
]