from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
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


@login_required
def profile_edit_view(request):

        if request.method == 'POST':
            user_update_form = UserUpdateForm(request.POST, instance=request.user)
            profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

            if user_update_form.is_valid() and profile_update_form.is_valid():
                user_update_form.save()
                profile_update_form.save()
                messages.success(request, 'Account Updated!')
                return redirect('profile')

        else:
            user_update_form = UserUpdateForm(instance=request.user)
            profile_update_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'user_update_form':user_update_form,
            'profile_update_form':profile_update_form,
            
            }

        return render(request, 'users/profile_edit.html', context)
