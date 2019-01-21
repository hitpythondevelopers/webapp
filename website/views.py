from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.

def welcome(request):
    return render(request, 'website/welcome.html')

def about_us(request):
    return render(request, 'website/about.html')
    
def emailView(request):
    if request.method == 'GET':
            form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email'] 
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['hitpythondevelopers@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "website/contact.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')