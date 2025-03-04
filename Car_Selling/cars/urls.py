from django.urls import path
from .views import CarsListView, CarsDetailView


urlpatterns = [
    path('', CarsListView.as_view(), name='cars-home'),
]