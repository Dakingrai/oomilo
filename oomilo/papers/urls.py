from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('papers/', views.papers, name="papers"),
]