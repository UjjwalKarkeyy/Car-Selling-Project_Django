from django.urls import path
from .views import CarsListView, CarsDetailView


urlpatterns = [
    path('', CarsListView.as_view(), name='cars-list'),
    path('car/<int:pk>/', CarsDetailView.as_view(), name='cars-detail'),
    # path('car/<int:pk>/', CarsDetailView.as_view(), name='category-detail'),

]