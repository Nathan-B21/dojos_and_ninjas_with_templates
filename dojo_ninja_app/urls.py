from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path("processDojo", views.processDojo),
    path("processNinja", views.processNinja)
]