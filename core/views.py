from django.shortcuts import render, redirect
from core.models import User
from .forms import EditProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
# Create your views here.

def index(request):
    return render(request, 'index.html')

def user_profile(request, username):
    user = User.objects.get(username=request.user)
    return render(request, 'core/user_profile.html', {"user":user})

def index(request):
    context = { 
    }
    return render(request, 'index.html', context=context)

def disclosure(request):
    context = {
    }
    return render(request, 'core/disclosure.html', context=context)

def create_group(request):
    context = {
    }
    return render(request, 'core/create_group.html', context=context)

# def edit_profile(request):
#     form = EditProfileForm(request.POST)
#     if form.is_valid():
#         form.save(user=request.user)
#     return render(request, 'edit_profile')

# class EditProfileView(LoginRequiredMixin, View):

#     def get(self, request):
#         form = EditProfileForm(request.POST)
#         if form.is_valid():
#             form.save(user=request.user)
#             return render(request, 'edit_profile.html')

