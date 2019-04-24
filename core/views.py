from django.shortcuts import render, redirect
from core.forms import NewGroupForm, EditProfileForm, NewTrackerInstanceForm, NewResponseForm, NewTrackerGroupForm, NewQuestionForm
from core.models import User, TrackerGroup, Question, Answer, Response, TrackerGroupInstance
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import Group
    # https://docs.djangoproject.com/en/2.2/topics/auth/default/#groups
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods


def index(request):
    return render(request, 'index.html')

def user_profile(request, username):
    user = User.objects.get(username=request.user)
    return render(request, 'core/user_profile.html', {"user":user})

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
            return HttpResponseRedirect(reverse('discover_page'))
    else:
        new_group_form = NewGroupForm()

    return render(request, 'core/create_group.html', {"form": new_group_form})

# class TrackerCreate(CreateView):
#     model = TrackerGroup
#     fields = '__all__'
#     template_name='core/trackergroup_create.html'

class NewTrackerView(LoginRequiredMixin, View):

    def dispatch(self, request, *args, **kwargs):
        self.question_form = NewQuestionForm()
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        last_tracker_created = TrackerGroup.objects.filter(created_by=request.user).last()
        last_question_created = Question.objects.filter(created_by=request.user).last()
        form = NewTrackerGroupForm()
        context = {
            "form": form,
            "question_form": self.question_form,
            "last_tracker_created": last_tracker_created,
            "last_question_created": last_question_created,
        }
        return render(request, "core/trackergroup_create.html", context)

    def post(self, request):
        last_tracker_created = TrackerGroup.objects.filter(created_by=request.user).last()
        last_question_created = Question.objects.filter(created_by=request.user).last()
        form = NewTrackerGroupForm(request.POST)
        if form.is_valid():
            tracker = form.save(created_by=request.user)
            query_dict_copy = request.POST.copy()
            available_to_keys = query_dict_copy.pop('available_to')
            for key in available_to_keys:
                tracker.available_to.add(User.objects.get(pk=key))
            return HttpResponseRedirect(reverse('tracker-detail', args=[str(tracker.id)]))
                #credit: https://stackoverflow.com/questions/50731218/django-str-object-has-no-attribute-get

        context = {
            "form": form,
            "question_form": self.question_form,
            "last_tracker_created": last_tracker_created,
            "last_question_created": last_question_created,
        }
        return render(request, "core/trackergroup_create.html", context)

@login_required
def create_tracker_questions(request):
    if request.method == 'POST':
        form = NewQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(created_by=request.user)
    return redirect('tracker-create')

class TrackerDetailView(generic.DetailView):
    model = TrackerGroup

class QuestionCreate(CreateView):
    model = Question
    fields = '__all__'
    template_name='core/question_create.html'

class QuestionDetailView(generic.DetailView):
    model = Question

class QuestionUpdate(UpdateView):
    model = Question
    template_name = 'question_edit'
    fields = ['tracker',
    'active',
    'question']


class AnswerCreate(CreateView):
    model = Answer
    fields = '__all__'
    template_name='core/answer_create.html'

class AnswerDetailView(generic.DetailView):
    model = Answer

class AnswerUpdate(UpdateView):
    model = Answer
    template_name = 'answer_edit'
    fields = ['question',
    'answer',
    'tracker']

def new_trackerinstance(request, tracker_pk):
    new_trackerinstance_form = NewTrackerInstanceForm()
    if request.method == 'POST':
        new_trackerinstance_form = NewTrackerInstanceForm(request.POST)
        if new_trackerinstance_form.is_valid():
            # tracker = request.POST.get('tracker', '') 
                # can't use this, since it returns a string
            tracker_instance = TrackerGroupInstance.objects.create(
                tracker_id=tracker_pk,
                created_by=request.user,
            )
            tracker_instance.save()
            
            return HttpResponseRedirect(reverse('trackergroupinstance_detail', args=[str(tracker_instance.id)]))
    else:
        new_trackerinstance_form = NewTrackerInstanceForm()
    return render(request, 'core/trackergroupinstance_create.html', {"form": new_trackerinstance_form})

class TrackerInstanceDetailView(generic.DetailView):
    model = TrackerGroupInstance

def new_response(request, question_pk, group_pk):
# def new_response(request, question_pk):
    # credit: https://stackoverflow.com/questions/291945/how-do-i-filter-foreignkey-choices-in-a-django-modelform
    question = get_object_or_404(Question, id=question_pk)
    group = get_object_or_404(Group, id=group_pk)
    if request.method == 'POST':
        # new_response_form = NewResponseForm(question_pk, request.POST)
        new_response_form = NewResponseForm(question_pk, group_pk, request.POST)
        if new_response_form.is_valid():
            tracker = question.tracker
            tracker_instance = tracker.tracker_instances.last()
                # need a better way to do this
            query_dict_copy = request.POST.copy()
                # https://docs.djangoproject.com/en/2.2/ref/request-response/#django.http.QueryDict
            answer_keys = query_dict_copy.pop('answer')
                # https://docs.djangoproject.com/en/2.2/ref/request-response/#django.http.QueryDict.pop
            answered_for_keys = query_dict_copy.pop('answered_for')
            answered_for = []
            for key in answered_for_keys:
                answered_for.append(key)

            response = Response.objects.create(
                answered_for_id=answered_for[0],
                question_id=question_pk,
                tracker_id=tracker.id,
                tracker_instance_id=tracker_instance.id,
            )
            for key in answer_keys:
                response.answer.add(Answer.objects.get(pk=key))
                
            response.save()
            
            return HttpResponseRedirect(reverse('trackergroupinstance_detail', args=[str(tracker_instance.id)]))
    else:
        # new_response_form = NewResponseForm(question_pk)
        new_response_form = NewResponseForm(question_pk, group_pk)
    
    context = {
        'form': new_response_form,
    }

    return render(request, 'core/response_create.html', context=context)

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

def user_detail(request, pk):
    template_name = 'core/user_detail.html'
    trackers = TrackerGroup.objects.filter(available_to=pk)
    context = {
        'trackers': trackers,
    }
    return render(request, 'core/user_detail.html', context)

def discover_page(request):
    users = User.objects.all()
    groups = Group.objects.all()

    context = {
        'users': users,
        'groups': groups,
    }
    return render(request, 'core/discover_page.html', context=context)

def quick_links(request):
    groups = Group.objects.all()
    trackers = TrackerGroup.objects.filter(available_to=request.user)

    context = {
        'groups': groups,
        'trackers': trackers,
    }
    return render(request, 'core/quick_links.html', context=context)

def references(request):
    return render(request, 'core/reference.html')
      
def calendar(request):
    return render(request, 'core/calendar.html')

### Unused Code ###
# def landing_page(request, username):
#     user = User.objects.get(username=username)
#     return render(request, 'core/landing_page.html', {"user":user})

# def create_group(request):
#     context = {
#     }
#     return render(request, 'core/create_group.html', context=context)