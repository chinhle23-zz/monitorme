from django.shortcuts import render

# Create your views here.

def user_profile(request, username):
    user = User.objects.all()
    return render(request, 'user_profile.html', {"user":user})

def index(request):
    context = { 
    }
    return render(request, 'index.html', context=context)
