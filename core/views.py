from django.shortcuts import render, redirect
from core.forms import NewGroupForm, NewTrackerInstanceForm, NewResponseForm, CreateTrackerQuestionAnswerForm, CreateQuestionAnswerForm, CreateAnswerForm, ResponseForm
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
from django.db.models import Avg, Count
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from django.forms import modelformset_factory, formset_factory
from django import forms
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def index(request):
    trackers = TrackerGroup.objects.all()

    context = {
        'trackers': trackers,
    }
    return render(request, 'index.html', context=context)

def references(request):
    context = {
    }
    return render(request, 'core/reference.html')


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
                current_question=question_description,
                tracker=tracker,
                created_by=request.user,
            )
            answer_name1 = request.POST.get('answer_name1', '')
            answer = Answer.objects.create(
                current_answer=answer_name1,
                question=question,
                created_by=request.user,
            )
            answer_name2 = request.POST.get('answer_name2', '')
            answer = Answer.objects.create(
                current_answer=answer_name2,
                question=question,
                created_by=request.user,
            )
            answer_name3 = request.POST.get('answer_name3', '')
            if (answer_name3 != ""):
                answer = Answer.objects.create(
                    current_answer=answer_name3,
                    question=question,
                    created_by=request.user,
                )
            return HttpResponseRedirect(reverse('tracker-all-detail', args=[tracker.id]))
        else:
            form = CreateTrackerQuestionAnswerForm()
    tracker = TrackerGroup.objects.filter(user=request.user).last
    context = {
        'form': form,
        'tracker': tracker,
    }
    return render(request, 'core/trackergroup_create.html', context=context)

@login_required
def question_create(request, pk):
    form = CreateQuestionAnswerForm()
    tracker = TrackerGroup.objects.get(pk=pk)
    if request.method == 'POST':
        form = CreateQuestionAnswerForm(request.POST)
        answer_form = CreateAnswerForm(request.POST)
        if form.is_valid:
            question_description = request.POST.get('question_description', '')
            question = Question.objects.create(
                current_question=question_description,
                tracker=tracker,
                created_by=request.user,
            )
            answer_name1 = request.POST.get('answer_name1', '')
            answer = Answer.objects.create(
                current_answer=answer_name1,
                question=question,
                created_by=request.user,
            )
            answer_name2 = request.POST.get('answer_name2', '')
            answer = Answer.objects.create(
                current_answer=answer_name2,
                question=question,
                created_by=request.user,
            )
            answer_name3 = request.POST.get('answer_name3', '')
            if (answer_name3 != ""):
                answer = Answer.objects.create(
                    current_answer=answer_name3,
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

@login_required
def answer_create(request, pk):
    form = CreateAnswerForm()
    question = Question.objects.get(pk=pk)
    if request.method == 'POST':
        form = CreateAnswerForm(request.POST)
        if form.is_valid:
            answer_name = request.POST.get('answer_name', '')
            answer = Answer.objects.create(
                current_answer=answer_name,
                question=question,
                created_by=request.user,
            )
            return HttpResponseRedirect(reverse('question-detail', args=[question.id]))
        else:
            form = CreateAnswerForm()
    context = {
        'form': form,
        'question': question,
    }
    return render(request, 'core/question_detail.html', context=context)

@login_required
def question_detail_create(request, pk):
    form = CreateQuestionAnswerForm()
    tracker = TrackerGroup.objects.get(pk=pk)
    if request.method == 'POST':
        form = CreateQuestionAnswerForm(request.POST)
        answer_form = CreateAnswerForm(request.POST)
        if form.is_valid:
            question_description = request.POST.get('question_description', '')
            question = Question.objects.create(
                current_question=question_description,
                tracker=tracker,
                created_by=request.user,
            )
            answer_name1 = request.POST.get('answer_name1', '')
            answer = Answer.objects.create(
                current_answer=answer_name1,
                question=question,
                created_by=request.user,
            )
            answer_name2 = request.POST.get('answer_name2', '')
            answer = Answer.objects.create(
                current_answer=answer_name2,
                question=question,
                created_by=request.user,
            )
            answer_name3 = request.POST.get('answer_name3', '')
            if (answer_name3 != ""):
                answer = Answer.objects.create(
                    current_answer=answer_name3,
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
    template_name = 'core/question_edit.html'
    fields = ['current_question']



class AnswerCreate(CreateView):
    model = Answer
    fields = '__all__'
    template_name = 'core/answer_create.html'


class AnswerDetailView(generic.DetailView):
    model = Answer


class AnswerUpdate(UpdateView):
    model = Answer
    template_name = 'core/answer_edit.html'
    fields = [
    'current_answer']


@login_required
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


def new_response(request, question_pk, answer_pk):
    question = get_object_or_404(Question, id=question_pk)
    tracker = question.tracker
    tracker_instance = tracker.tracker_instances.last()
    if request.method == 'POST':
        response = Response.objects.create(
            question_id=question_pk,
            tracker_id=tracker.id,
            tracker_instance_id=tracker_instance.id,
            user = request.user,
        )
        response.answers.add(Answer.objects.get(pk=answer_pk))
        response.save()
        return HttpResponseRedirect(reverse('trackergroupinstance_detail', args=[str(tracker_instance.id)]))
    else:
        new_response_form = NewResponseForm(question_pk)
    context = {
        'form': new_response_form,
    }
    return render(request, 'core/response_create.html', context=context)


#### Chinh will come back to this later to implement formsets#####
def response_create(request):
    ResponseFormSet = formset_factory(ResponseForm(12), extra=2)
        # https://docs.djangoproject.com/en/2.2/topics/forms/formsets/
    formset = ResponseFormSet()
    # form = ResponseForm(12)
    context = {
        'formset': formset,
        # 'form': form,
    }

    return render(request, 'core/response_create.html', context)

    #### old response_create notes ####
        # credit: https://www.youtube.com/watch?v=FnZgy-y6hGA&feature=youtu.be
    # instance = TrackerGroupInstance.objects.create(
    #     tracker_id=tracker_id,
    #     created_by=request.user,
    # )
    # tracker = TrackerGroup.objects.get(id=12)
    # questions = tracker.questions.all()
    # # ResponsesFormSet = modelformset_factory(Response, fields=('question', 'answers'), extra=len(questions))
    # # ResponsesFormSet = modelformset_factory(ResponseForm, fields=('answers',), extra=len(questions))
    # ResponseFormSet = modelformset_factory(Response,
    #     form=ResponseForm, 
    # )
    # form = ResponseFormSet(

    # )
    # form = ResponseFormSet(
    #     # initial=[{'question': question} for question in questions],
    # )
    # if request.method == 'POST':
    # form = ResponseForm(12)
#### Chinh will come back to this later to implement formsets#####
   
  
def response_detail(request, pk):
    context = {
    }
    return render(request, 'response_detail', context=context)

def report_detail(request, pk):
    template_name = 'core/report.html'

    #This is to filter user informatian only
    user_info = User.objects.filter(pk=request.user.pk)

    #This is to filter only users trackers
    trackers = TrackerGroup.objects.filter(user=request.user)

    #This is to filter all instances by user
    instances = TrackerGroupInstance.objects.filter(created_by=request.user).order_by('-started_at')
    paginator = Paginator(instances, 5)
    
    page = request.GET.get('page')
    tracker_instances = paginator.get_page(page)

    #Responses from user only
    responses = Response.objects.filter(user=request.user)

    context = {
        'user_info': user_info,
        'trackers': trackers, 
        'instances': instances,
        'responses': responses,
        'tracker_instances': tracker_instances,
    }
    
    return render(request, 'core/report.html', context=context)

def references(request):
    context = {
    }
    return render(request, 'core/reference.html')

      


# UNUSED CODE, SAVING FOR LATER REFACTORING
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


# class TrackerCreate(CreateView):
#     model = TrackerGroup
#     fields = '__all__'
#     template_name='core/trackergroup_create.html'
def report(request):

    return render(request, 'core/report.html', context=context)

def about_us(request):
    template_name = 'core/about_us.html'
    context = {
    }	 

    return render(request, 'core/about_us.html', context=context)

class ResponseDelete(DeleteView):
    model = Response
    success_url = reverse_lazy('delete-successful')


class QuestionDelete(DeleteView):
    model = Question
    success_url = reverse_lazy('delete-successful')

class AnswerDelete(DeleteView):
    model = Answer
    success_url = reverse_lazy('delete-successful')

class TrackerGroupInstanceDelete(DeleteView):
    model = TrackerGroupInstance
    success_url = reverse_lazy('delete-successful')

class TrackerGroupDelete(DeleteView):
    model = TrackerGroup
    success_url = reverse_lazy('delete-successful')

def response_detail2(request, pk):
    instances = TrackerGroupInstance.objects.filter(pk=pk)

    responses = Response.objects.filter(user=request.user, tracker_instance=pk)

    context = {
        'instances': instances,
        'responses': responses,
    }

    return render(request, 'core/response_detail2.html', context=context)

def delete_message(request):
    return render(request, 'core/delete_confirmation.html')
    