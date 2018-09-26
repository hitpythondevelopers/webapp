from django.shortcuts import render, redirect
from .forms import ContactForm


# Create your views here.

def welcome(request):
    return render(request, 'website/welcome.html')

def about_us(request):
    return render(request, 'website/about.html')
    

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})