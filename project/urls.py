from django.urls import path
from . import views

urlpatterns = [
    path('', views.projectHome, name='projectHome'),
]
