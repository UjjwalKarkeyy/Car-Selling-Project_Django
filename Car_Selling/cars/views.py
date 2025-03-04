from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Cars

class CarsListView(ListView):
    model = Cars

class CarsDetailView(DetailView):
    pass

