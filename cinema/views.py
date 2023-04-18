from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import *

def index(request):
    return render(request, 'cinema/index.html',{
        
    })

