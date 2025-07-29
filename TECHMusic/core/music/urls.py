from . import views
from django.urls import path

urlpatterns = [
    path('songs/', views.MusicListView.as_view())
]