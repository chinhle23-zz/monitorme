from django.shortcuts import render
from core.models import User, TrackerGroup, Question, Answer, Response
# Create your views here.

def user_profile(request, username):
    user = User.objects.all()
    return render(request, 'user_profile.html', {"user":user})
