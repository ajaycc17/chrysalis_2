from xml.dom.minidom import Document
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.blogPage, name='BlogPage'),
    path('postComment/', views.postComment, name='postComment'),
    path('topics/', views.topics, name='topics'),
    path('<str:slug>/', views.blogPost, name='BlogPost'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
