# Imports
from django.urls import path
from . import views

# Paths
urlpatterns = [
    path('', views.home, name = "blog-home"),
    path('about/', views.about, name = "blog-about"),
]