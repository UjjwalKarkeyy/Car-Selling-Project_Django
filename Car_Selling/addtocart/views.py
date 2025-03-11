from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cart, Cars
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

class CarsOnCartView(LoginRequiredMixin, ListView):
    model = Cart
    context_object_name = 'cart'

@login_required
def add_to_cart(request, pk):

    car = get_object_or_404(Cars, pk = pk)

    item, created = Cart.objects.get_or_create(user = request.user, car = car)

    if created:
        return JsonResponse({"message": "Item added to cart!", "status": "success"})
    else:
        return JsonResponse({"message": "Item already in cart!", "status": "warning"})