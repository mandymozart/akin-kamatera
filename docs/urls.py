# docs/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name='hello_world'),
]