from django.urls import path
from .views import TemperaturaAPIView

urlpatterns = [
    path('temperatura', TemperaturaAPIView.as_view()),
    path('temperatura/<str:pk>', TemperaturaAPIView.as_view()) 
]