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
# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', core_views.index, name='index'),
    path('disclosure/', core_views.disclosure, name='disclosure'),
    path('create_group/', core_views.create_group, name='create_group'),
    path('profile/<username>', core_views.user_profile, name="user_profile"),
    path('discover/', core_views.discover_page, name="discover_page"),
    path('tracker/<int:pk>', core_views.TrackerDetailView.as_view(), name="tracker-detail"),
    path('response_detail', core_views.response_detail, name= 'response_detail'),
    path('dashboard_detail/', core_views.dashboard_detail, name= 'dashboard_detail'),
    path('tracker/create/', core_views.TrackerCreate.as_view(), name="tracker-create"),
    path('tracker/question/create/', core_views.QuestionCreate.as_view(), name="question-create"),
    path('tracker/answer/create/', core_views.AnswerCreate.as_view(), name="answer-create"),
    path('calendar/', core_views.calendar, name="calendar"),
    path('user_detail/<int:pk>', core_views.user_detail, name="user-detail"),
    path('references/', core_views.references, name="references"),
    path('profile/<int:pk>/update', core_views.UserUpdate.as_view(), name="edit-profile"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# team has agreed to only use one urls.py file

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
       path('__debug__/', include(debug_toolbar.urls)),
   ] + urlpatterns

