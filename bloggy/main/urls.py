from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('Blog', views.blog, name='blog'),
    path('Blog/<str:post_name>/', views.post, name='post'),
]