from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import *

def index(request):
    return render(request, 'cinema/index.html',{
        
    })

def registration(request):
    if request.method == 'POST':
        username       = request.POST['username']
        first_name     = request.POST['first_name']
        last_name      = request.POST['last_name']
        email          = request.POST['email']
        password       = request.POST['password']
        confirmation   = request.POST['confirmation']
        if confirmation != password:
            pass
    
        else:
            user = Users.objects.create_user(username,email,password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'cinema/Registration&login.html')


def registration_page(request):
    return render(request, 'cinema/Registration&login.html',{

    })