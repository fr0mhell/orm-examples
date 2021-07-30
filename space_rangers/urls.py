from django.urls import path
from . import views

urlpatterns = [
    path('spaceships/', views.SpaceshipCreateView.as_view()),
    path('spaceships/<int:pk>/', views.SpaceshipDetailView.as_view()),
]
