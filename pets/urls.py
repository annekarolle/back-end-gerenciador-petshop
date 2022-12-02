from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("pets/", views.PetView.as_view()),
    path("pets/<int:pet_id>/", views.PetDetailView.as_view()),
]