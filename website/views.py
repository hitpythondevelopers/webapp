from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.

def welcome(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'website/about.html')
    
