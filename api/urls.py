from django.urls import path
from . import views

urlpatterns = [
    path('festivals', views.getFestivals)
]