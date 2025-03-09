from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

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


class UpdatedPasswordResetView(auth_views.PasswordResetView):
    def form_valid(self, form):
        
        self.request.session['password_reset_initiated'] = True
        return super().form_valid(form)

class UpdatedPasswordResetDoneView(auth_views.PasswordResetDoneView):
    def dispatch(self, request, *args, **kwargs):

        if not request.session.get('password_reset_initiated'):
            return redirect('password_reset')
        
        return super().dispatch(request, *args, **kwargs)
    
class UpdatedPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    def dispatch(self, request, *args, **kwargs):

        if not request.session.get('password_reset_initiated'):
            return redirect('password_reset')

        return super().dispatch(request, *args, **kwargs)
    
class UpdatedPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    def dispatch(self, request, *args, **kwargs):

        if not request.session.get('password_reset_initiated'):
            return redirect('password_reset')

        return super().dispatch(request, *args, **kwargs)
    
    