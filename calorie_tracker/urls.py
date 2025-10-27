from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('remove/<int:pk>/', views.remove_food, name='remove_food'),
    path('reset/', views.reset_calories, name='reset_calories'),
]
