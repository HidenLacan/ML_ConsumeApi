
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('aguacate_prediccion/', views.Agucate_prediccion.as_view(),name='aguacate_prediccion'),
]