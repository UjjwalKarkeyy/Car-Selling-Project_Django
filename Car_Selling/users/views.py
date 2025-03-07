from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')

def register_view(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created. Log In!')
            return redirect('login')

    else:
        form = UserRegisterForm()

    context = {'form':form}

    return render(request, 'users/register.html', context)

@login_required
def profile_view(request):
    return render(request, 'users/profile.html')



