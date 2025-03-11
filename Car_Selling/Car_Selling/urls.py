"""
URL configuration for Car_Selling project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users.views import (logout_view, 
                         register_view, profile_view, 
                         profile_edit_view, UpdatedPasswordResetView,
                         UpdatedPasswordResetDoneView, UpdatedPasswordResetConfirmView,
                         UpdatedPasswordResetCompleteView)
from addtocart.views import CarsOnCartView, add_to_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cars.urls')),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name= 'login'),
    path('password_reset/', UpdatedPasswordResetView.as_view(template_name = 'users/password_reset.html'), name= 'password_reset'),
    path('password_reset/done/', UpdatedPasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html'), name= 'password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', UpdatedPasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'), name= 'password_reset_confirm'),
    path('password_reset/complete/', UpdatedPasswordResetCompleteView.as_view(template_name = 'users/password_reset_complete.html'), name= 'password_reset_complete'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit', profile_edit_view, name='profile-edit'),
    path('cart/', CarsOnCartView.as_view(), name='cart'),
    path('cart/add/<pk>/', add_to_cart, name='cart-add'),
]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
