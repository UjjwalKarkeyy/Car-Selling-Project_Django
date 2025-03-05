from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Cars

class CarsListView(ListView):
    model = Cars
    context_object_name = 'cars'

class CarsDetailView(DetailView):
    pass

