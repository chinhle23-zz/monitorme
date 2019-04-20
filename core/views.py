from django.shortcuts import render, redirect
from core.models import User, TrackerGroup, Question, Answer
from core.forms import NewGroupForm, EditProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import Group
    # https://docs.djangoproject.com/en/2.2/topics/auth/default/#groups
from django.http import HttpResponseRedirect

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

### Chinh's version ####
def new_group(request):
    new_group_form = NewGroupForm()
    if request.method == 'POST':
        new_group_form = NewGroupForm(request.POST)
        if new_group_form.is_valid():
            # https://docs.djangoproject.com/en/2.2/ref/forms/api/#django.forms.Form.is_valid
            name = request.POST.get('name', '')
                # https://docs.djangoproject.com/en/2.1/ref/request-response/#django.http.HttpRequest.POST
                # https://docs.djangoproject.com/en/2.1/ref/request-response/#django.http.QueryDict.get
            group = Group.objects.create(
                name=name,
            )
            group.save()
            return HttpResponseRedirect(reverse('landing_page', kwargs={'username': request.user.username,} ))
    else:
        new_group_form = NewGroupForm()

    return render(request, 'core/group_form.html', {"form": new_group_form})

# ### Chinh's version ####
# class CreateGroup(LoginRequiredMixin, CreateView):
#     """
#     Form for creating a group. Requires login. 
#     """
#     model = Group
#         # define the associated model
#     fields = ['name', ]
#         # specify the fields to dislay in the form

# #### Chinh's version ####
# class NameGroupDetailView(generic.DetailView):
#     """View class for NameGroup detail page of site."""
#     model = NameGroup

# def landing_page(request):
#     context = {
#     }
#     return render(request, 'landing_page', context=context)

# def response_detail(request):
#     context = {
#     }
#     return render(request, 'response_detail', context=context)

# def dashboard_detail(request):
#     # Chinh added 4/19/2019:
#     namegroups = NameGroup.objects.filter(users__username=request.user.username)
#     trackergroups = TrackerGroup.objects.filter(available_to__username=request.user.username)
#         # https://docs.djangoproject.com/en/2.2/topics/db/queries/#lookups-that-span-relationships

#     context = {
#         # Chinh added 4/19/2019:
#         'namegroups': namegroups,
#         'trackergroups': trackergroups,
#     }

#     return render(request, 'core/dashboard_detail.html', context=context)

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

#### Chinh's version ####
# class CreateTracker(LoginRequiredMixin, CreateView):
#     """
#     Form for creating a tracker. Requires login. 
#     """
#     model = TrackerGroup
#         # define the associated model
#     fields = ['name', 'available_to']
#         # specify the fields to dislay in the form

class QuestionCreate(CreateView):
    model = Question
    fields = '__all__'
    template_name='core/question_create.html'    

class AnswerCreate(CreateView):
    model = Answer
    fields = '__all__'
    template_name='core/answer_create.html'      

def calendar(request):
    return render(request, 'core/calendar.html')


    
