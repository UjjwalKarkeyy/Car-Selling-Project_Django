from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms

class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password1']

class UserUpdateForm(forms.ModelForm):
    
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    
    image = forms.ImageField(label='Profile Picture', widget=forms.FileInput(attrs={'class':'form-control'}), required=False)

    class Meta:
        model = Profile
        fields = ['image']
