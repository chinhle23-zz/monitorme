from django.shortcuts import render, redirect
from core.forms import NewGroupForm, EditProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.shortcuts import render
from core.models import User, TrackerGroup, Question, Answer, Response
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

    return render(request, 'core/create_group.html', {"form": new_group_form})

# Chinh copied from kt-dashboard-page 4/20/2019:
def dashboard_detail(request):
    group_name = Group.objects.filter(user=request.user)
    user_group = group_name[0]
    users = User.objects.filter(groups__name=user_group)
    trackers = TrackerGroup.objects.all()

    context = {
        'users': users,
        'trackers': trackers,
        'group_name': group_name,
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

#### Chinh's version ####
# class CreateTracker(LoginRequiredMixin, CreateView):
#     """
#     Form for creating a tracker. Requires login. 
#     """
#     model = TrackerGroup
#         # define the associated model
#     fields = ['name', 'available_to']
#         # specify the fields to dislay in the form

# Chinh added 4/20/2019
class QuestionDetailView(generic.DetailView):
    model = Question

class QuestionCreate(CreateView):
    model = Question
    fields = '__all__'
    template_name='core/question_create.html'    

# Chinh added 4/20/2019
class AnswerDetailView(generic.DetailView):
    model = Answer

class AnswerCreate(CreateView):
    model = Answer
    fields = '__all__'
    template_name='core/answer_create.html'      

def calendar(request):
    return render(request, 'core/calendar.html')

def user_detail(request, pk):
    template_name = 'core/user_detail.html'
    trackers = TrackerGroup.objects.filter(available_to=pk)

    context = {
        'trackers': trackers,
    }

    return render(request, 'core/user_detail.html', context)




    
