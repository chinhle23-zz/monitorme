from django.shortcuts import render, redirect
from core.forms import NewGroupForm, NewTrackerInstanceForm, NewResponseForm, CreateTrackerQuestionAnswerForm, CreateQuestionAnswerForm, CreateAnswerForm
from core.models import User, TrackerGroup, Question, Answer, Response, TrackerGroupInstance
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import Group
    # https://docs.djangoproject.com/en/2.2/topics/auth/default/#groups
from django.http import HttpResponseRedirect



def index(request):
    trackers = TrackerGroup.objects.all()

    context = {
        'trackers': trackers,
    }
    return render(request, 'index.html', context=context)

def user_profile(request, username):
    user = User.objects.get(username=request.user)
    return render(request, 'core/user_profile.html', {"user":user})

class UserUpdate(UpdateView):
    model = User
    template_name = 'core/edit_profile.html'
    fields = (
        'name',
        'email',
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

def tracker_create(request):
    form = CreateTrackerQuestionAnswerForm()
    if request.method == 'POST':
        form = CreateTrackerQuestionAnswerForm(request.POST)
        if form.is_valid:
            tracker_name = request.POST.get('tracker_name', '')
            tracker = TrackerGroup.objects.create(
                name=tracker_name,
                user=request.user,
            )
            question_description = request.POST.get('question_description', '')
            question = Question.objects.create(
                tracker_question=question_description,
                tracker=tracker,
                created_by=request.user,
            )
            answer_name1 = request.POST.get('answer_name1', '')
            answer = Answer.objects.create(
                question_answer=answer_name1,
                question=question,
                created_by=request.user,
            )
            answer_name2 = request.POST.get('answer_name2', '')
            answer = Answer.objects.create(
                question_answer=answer_name2,
                question=question,
                created_by=request.user,
            )
            answer_name3 = request.POST.get('answer_name3', '')
            answer = Answer.objects.create(
                question_answer=answer_name3,
                question=question,
                created_by=request.user,
            )
            return HttpResponseRedirect(reverse('tracker-detail', args=[tracker.id]))
        else:
            form = CreateTrackerQuestionAnswerForm()
    tracker = TrackerGroup.objects.filter(user=request.user).last
    context = {
        'form': form,
        'tracker': tracker,
    }
    return render(request, 'core/trackergroup_create.html', context=context)



def question_create(request, pk):
    form = CreateQuestionAnswerForm()
    tracker = TrackerGroup.objects.get(pk=pk)
    if request.method == 'POST':
        form = CreateQuestionAnswerForm(request.POST)
        answer_form = CreateAnswerForm(request.POST)
        if form.is_valid:
            question_description = request.POST.get('question_description', '')
            question = Question.objects.create(
                tracker_question=question_description,
                tracker=tracker,
                created_by=request.user,
            )
            answer_name1 = request.POST.get('answer_name1', '')
            answer = Answer.objects.create(
                question_answer=answer_name1,
                question=question,
                created_by=request.user,
            )
            answer_name2 = request.POST.get('answer_name2', '')
            answer = Answer.objects.create(
                question_answer=answer_name2,
                question=question,
                created_by=request.user,
            )
            answer_name3 = request.POST.get('answer_name3', '')
            answer = Answer.objects.create(
                question_answer=answer_name3,
                question=question,
                created_by=request.user,
            )
            return HttpResponseRedirect(reverse('tracker-detail', args=[tracker.id]))
        else:
            form = CreateQuestionAnswerForm()
    context = {
        'form': form,
        'tracker': tracker,
    }
    return render(request, 'core/trackergroup_detail.html', context=context)


def question_detail_create(request, pk):
    form = CreateQuestionAnswerForm()
    tracker = TrackerGroup.objects.get(pk=pk)
    if request.method == 'POST':
        form = CreateQuestionAnswerForm(request.POST)
        answer_form = CreateAnswerForm(request.POST)
        if form.is_valid:
            question_description = request.POST.get('question_description', '')
            question = Question.objects.create(
                tracker_question=question_description,
                tracker=tracker,
                created_by=request.user,
            )
            answer_name1 = request.POST.get('answer_name1', '')
            answer = Answer.objects.create(
                question_answer=answer_name1,
                question=question,
                created_by=request.user,
            )
            answer_name2 = request.POST.get('answer_name2', '')
            answer = Answer.objects.create(
                question_answer=answer_name2,
                question=question,
                created_by=request.user,
            )
            answer_name3 = request.POST.get('answer_name3', '')
            answer = Answer.objects.create(
                question_answer=answer_name3,
                question=question,
                created_by=request.user,
            )
            return HttpResponseRedirect(reverse('tracker-all-detail', args=[tracker.id]))
        else:
            form = CreateQuestionAnswerForm()
    context = {
        'form': form,
        'tracker': tracker,
    }
    return render(request, 'core/trackergroup_all_detail.html', context=context)

# def answer_create(request, pk):
#     form = CreateAnswerForm()
#     question = question.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = CreateQuestionAnswerForm(request.POST)
#         if form.is_valid:
#             answer_name = request.POST.get('answer_name', '')
#             answer = Answer.objects.create(
#                 name=answer_name1,
#                 question=question,
#                 created_by=request.user,
#             )
#             return HttpResponseRedirect(reverse('tracker-detail', args=[tracker.id]))
#         else:
#             form = CreateQuestionAnswerForm()
#     context = {
#         'form': form,
#         'tracker': tracker,
#     }
#     return render(request, 'core/trackergroup_detail.html', context=context)

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

def new_response(request, question_pk):
# def new_response(request, question_pk):
    # credit: https://stackoverflow.com/questions/291945/how-do-i-filter-foreignkey-choices-in-a-django-modelform
    question = get_object_or_404(Question, id=question_pk)
    if request.method == 'POST':
        # new_response_form = NewResponseForm(question_pk, request.POST)
        new_response_form = NewResponseForm(question_pk, request.POST)
        if new_response_form.is_valid():
            tracker = question.tracker
            tracker_instance = tracker.tracker_instances.last()
                # need a better way to do this

            response = Response.objects.create(
                question_id=question_pk,
                tracker_id=tracker.id,
                tracker_instance_id=tracker_instance.id,
                user = request.user,
            )

            response.save()
            
            return HttpResponseRedirect(reverse('trackergroupinstance_detail', args=[str(tracker_instance.id)]))
    else:
        # new_response_form = NewResponseForm(question_pk)
        new_response_form = NewResponseForm(question_pk)
    
    context = {
        'form': new_response_form,
    }

    return render(request, 'core/response_create.html', context=context)

def response_detail(request, pk):
    context = {
    }
    return render(request, 'response_detail', context=context)

def user_detail(request, pk):
    template_name = 'core/user_detail.html'
    user_info = User.objects.all()
    trackers = TrackerGroup.objects.all()
    questions = Question.objects.all()
    answers = Answer.objects.all()
    instances = TrackerGroupInstance.objects.all()
    responses = Response.objects.all()


    context = {
        'user_info': user_info,
        'trackers': trackers, 
        'questions': questions,
        'answers': answers,
        'instances': instances,
        'responses': responses,
    }

    return render(request, 'core/report.html', context=context)

def discover_page(request):
    users = User.objects.all()
    groups = Group.objects.all()

    context = {
        'users': users,
        'groups': groups,
    }
    return render(request, 'core/discover_page.html', context=context)


def references(request):
    return render(request, 'core/reference.html')
      
def report(request):

    return render(request, 'core/report.html', context=context)

### Unused Code ###
# def landing_page(request, username):
#     user = User.objects.get(username=username)
#     return render(request, 'core/landing_page.html', {"user":user})

# def create_group(request):
#     context = {
#     }
#     return render(request, 'core/create_group.html', context=context)