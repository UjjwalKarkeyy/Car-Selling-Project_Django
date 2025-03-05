from django.urls import path
from .views import CarsListView, CarsDetailView, CategoryListView


urlpatterns = [
    path('', CarsListView.as_view(), name='cars-list'),
    path('car/<int:pk>/', CarsDetailView.as_view(), name='cars-detail'),
    path('car-category/<str:category>/', CategoryListView.as_view(), name='category-list'),
]