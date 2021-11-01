from django.urls import include, path
from elsys import views

urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('about', views.about),
    path('cars', views.cars),
    path('api/v1/cars', views.cars_json),
]
