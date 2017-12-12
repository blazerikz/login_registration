from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
from datetime import datetime

# Create your views here.

def index(request):    
    return render(request,'login/index.html')

def success(request):    
    return render(request,'login/success.html')

def register(request):
    return redirect('/success')

def login(request):
    return redirect('/success')

def logout(request):
    return redirect('/')