from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            user = form.save()
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Join our Slack community'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return redirect('member_login')
    else:
        form = SignUpForm()
    return render(request, 'member/signup.html', {'form': form})


@login_required
def home(request):
    return render(request, 'member/home.html')


@login_required
def portfolio(request):
    return render(request, 'member/portfolio.html')