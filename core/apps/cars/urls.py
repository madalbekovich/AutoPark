from django.urls import path
from . import views

urlpatterns = [
    path('select-car/', views.CarDataListView.as_view()),
    path('public-data/', views.PublicDataView.as_view())
]