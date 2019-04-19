from django.shortcuts import render, redirect
from core.models import User
from .forms import EditProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.shortcuts import render
from core.models import User, TrackerGroup
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse, reverse_lazy

# Create your views here.

def index(request):
    return render(request, 'index.html')

def user_profile(request, username):
    user = User.objects.get(username=request.user)
    return render(request, 'core/user_profile.html', {"user":user})

def disclosure(request):
    context = {
    }
    return render(request, 'core/disclosure.html', context=context)

def create_group(request):
    context = {
    }
    return render(request, 'core/create_group.html', context=context)

def landing_page(request):
    context = {
    }
    return render(request, 'landing_page', context=context)

def response_detail(request):
    context = {
    }
    return render(request, 'response_detail', context=context)

def dashboard_detail(request):
    context = {
    }
    return render(request, 'core/dashboard_detail.html', context=context)
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


def landing_page(request, username):
    user = User.objects.get(username=username)
    return render(request, 'core/landing_page.html', {"user":user})

class TrackerDetailView(generic.DetailView):
    model = TrackerGroup


class TrackerCreate(CreateView):
    model = TrackerGroup
    fields = '__all__'
    template_name='core/trackergroup_create.html'

def calendar(request):
    return render(request, 'core/calendar.html')


    
