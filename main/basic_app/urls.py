from django.urls import path
from . import views

urlpatterns = [
    path('getbuslocationdec/', views.getBusLocationDec),
    path('getPolyLine/', views.getPolyLine),
    path('postbusdriverlocation/', views.postBusDriverLocation)
]
