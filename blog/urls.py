from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogPage, name='BlogPage'),
    path('postComment/', views.postComment, name='postComment'),
    path('topics/', views.topics, name='topics'),
    path('<str:slug>/', views.blogPost, name='BlogPost'),
]
