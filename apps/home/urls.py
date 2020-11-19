"""
Casino Apps URLs
"""
from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('add-new-application', views.AddView.as_view(), name="add"),
]