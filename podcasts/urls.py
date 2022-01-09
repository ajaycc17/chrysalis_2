from django.urls import path
from . import views

urlpatterns = [
    path('', views.podcastsHome, name='podcastsHome'),
    path('<str:slug>/', views.singlePodcast, name='singlePodcast'),
]
