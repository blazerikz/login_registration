# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def index(request):    
    return render(request,'book_reviews/index.html')

def addBook(request):
    return render(request,'book_reviews/addBook.html')

def showBook(request):    
    return render(request,'book_reviews/showBook.html')