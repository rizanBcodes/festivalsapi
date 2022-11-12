from django.urls import path
from . import views

urlpatterns = [
    path('festivals', views.getFestivals)
]

#need to add pagination/ some way to filter festivals by id