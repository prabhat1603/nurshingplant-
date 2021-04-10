from django.shortcuts import render, redirect, get_object_or_404,reverse
from django.contrib.auth import authenticate
from django.contrib import messages
from User.serializers import *


def SignUp(request):
    form = SignUpForm()
    if request.method  == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userstatus')
    context = {
        'form':form
    }
    return render(request, 'signup.html',context)
