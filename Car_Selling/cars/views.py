from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Cars

class CarsListView(ListView):
    model = Cars
    context_object_name = 'cars'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Cars.objects.values_list('category', flat = True).distinct()
        cars_by_category = {category: Cars.objects.filter(category = category) for category in categories}

        context['cars_by_category'] = cars_by_category

        return context


class CarsDetailView(DetailView):
    pass

