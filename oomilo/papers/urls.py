from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('papers/', views.papers, name="papers"),
    path('tags/', views.tags, name="tags"),
    path('tags/<int:tag_id>/', views.tag, name='tag'),
]