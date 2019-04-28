"""monitorme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.index, name='index'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('profile/<username>', core_views.user_profile, name="user_profile"),
    path('profile/<int:pk>/update', core_views.UserUpdate.as_view(), name="edit-profile"),
    path('group/add', core_views.new_group, name='group_form'),
    # path('tracker/create/', core_views.TrackerCreate.as_view(), name="tracker-create"),
    path('tracker/create/', core_views.tracker_create, name="tracker-create"),
    # path('tracker/<int:pk>', core_views.TrackerDetailView.as_view(), name="tracker-detail"),
    path('tracker/<int:pk>', core_views.question_create, name="tracker-detail"),
    path('tracker/<int:pk>/all/', core_views.question_detail_create, name="tracker-all-detail"),
    path('question/create/', core_views.QuestionCreate.as_view(), name="question-create"),
    path('question/<int:pk>/', core_views.QuestionDetailView.as_view(), name='question-detail'),
    path('answer/create/', core_views.AnswerCreate.as_view(), name="answer-create"),
    path('answer/<int:pk>', core_views.AnswerDetailView.as_view(), name="answer-detail"),
    path('answer/<int:pk>/update/', core_views.AnswerUpdate.as_view(), name="edit-answer"),
    path('trackerinstance/create/<int:tracker_pk>', core_views.new_trackerinstance, name="trackerinstance_create"),
    path('trackerinstance/<int:pk>', core_views.TrackerInstanceDetailView.as_view(), name="trackergroupinstance_detail"),
    path('response/create/<int:question_pk>/<int:answer_pk>', core_views.new_response, name="response_create"),
    path('response/create/', core_views.response_create, name="response_create"),
    path('response_detail/<int:pk>', core_views.response_detail, name= 'response_detail'),
    path('user_detail/<int:pk>', core_views.report_detail, name="user-detail"),
    path('sendemail/<int:pk>', core_views.email_report, name='send-email'),
    path('references/', core_views.references, name="references"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
       path('__debug__/', include(debug_toolbar.urls)),
   ] + urlpatterns

