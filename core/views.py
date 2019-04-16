from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'index.html')

def user_profile(request, username):
    user = User.objects.all()
    return render(request, 'user_profile.html', {"user":user})

def index(request):
    context = { 
    }
    return render(request, 'index.html', context=context)
