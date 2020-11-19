"""
Casino Apps URLs
"""
from django.urls import path

from . import views

app_name = "casino"

urlpatterns = [
    path("home", views.IndexView.as_view(), name="home"),
    path("start", views.GameView.as_view(), name="start")
]