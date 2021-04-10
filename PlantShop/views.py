from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect
from User.serializers import UserForm
from django.shortcuts import render

@login_required
@api_view(['GET'])
def Home(request):
    context = {
    'message' : 'Jump to the respective urls',
    'nursery' : '/Nursery/',
    'plant' : '/Plant/',
    'user' : '/User/'
    }
    return Response(context)


@api_view(['GET'])
def WelcomePage(request):
    if request.user.is_authenticated:
        context = {
        'message' : 'You are active',
        'logout' : '/logout/'
        }
    else:
        context = {
        'message' : 'Register yourself to explore this app',
        'Login Here if already registered' : '/login/',
        'Register here' : '/signup/',
        }
    return Response(context)

def LogoutView(request):
    return render(request, 'logout.html')

def UserStatus(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'userstatus.html', {'form' : form})
