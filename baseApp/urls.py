from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="baseApp_home"),
    path('room/<str:pk>/', views.room, name="baseApp_room"),
    path('about/', views.about, name="baseApp_about")
]