from django.shortcuts import render
from core.models import User, TrackerGroup
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse, reverse_lazy

# Create your views here.

def index(request):
    return render(request, 'index.html')

def user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'core/user_profile.html', {"user":user})


def landing_page(request, username):
    user = User.objects.get(username=username)
    return render(request, 'core/landing_page.html', {"user":user})

class TrackerDetailView(generic.DetailView):
    model = TrackerGroup


class TrackerCreate(CreateView):
    model = TrackerGroup
    fields = '__all__'
    template_name='core/trackergroup_create.html'


    
