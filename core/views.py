from django.shortcuts import render, redirect
from core.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.shortcuts import render
from core.models import User, TrackerGroup, Question, Answer, Response
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import Group


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

def discover_page(request):
    users = User.objects.all()
    groups = Group.objects.all()

    context = {
        'users': users,
        'groups': groups,
    }
    return render(request, 'core/discover_page.html', context=context)

def response_detail(request):
    context = {
    }
    return render(request, 'response_detail', context=context)

def dashboard_detail(request):
    group_name = Group.objects.filter(user=request.user)
    trackers = TrackerGroup.objects.all()
    
    if group_name == "":
        users = User.objects.all()
    else:
        user_group = group_name[0]
        users = User.objects.filter(groups__name=user_group)  

    context = {
        'users': users,
        'trackers': trackers,
        'group_name': group_name,
    }

    return render(request, 'core/dashboard_detail.html', context=context)


class TrackerDetailView(generic.DetailView):
    model = TrackerGroup


class TrackerCreate(CreateView):
    model = TrackerGroup
    fields = '__all__'
    template_name='core/trackergroup_create.html'

def calendar(request):
    return render(request, 'core/calendar.html')

def user_detail(request, pk):
    template_name = 'core/user_detail.html'
    trackers = TrackerGroup.objects.filter(available_to=pk)

    context = {
        'trackers': trackers,
    }

    return render(request, 'core/user_detail.html', context)

def references(request):
    return render(request, 'core/reference.html')

class UserUpdate(UpdateView):
    model = User
    template_name = 'core/edit_profile.html'
    fields = (
        'name',
        'email',
        'is_family_admin',
        'label',
        'city',
        'state',
        'zipcode',
        'active',
        'phonenumber',
        'groups',
    )
    success_url = ('/profile/{{user.username}}')

     


# Moved all commented out code to the bottom
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


# def landing_page(request, username):
#     user = User.objects.get(username=username)
#     return render(request, 'core/landing_page.html', {"user":user})

    
