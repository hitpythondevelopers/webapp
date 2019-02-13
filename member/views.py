from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login, authenticate
from .forms import SlackForm
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def slack_up(request):
    if request.method == 'POST':
        form = SlackForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            user.save()
            
    else:
        form = SlackForm
    return render(request, 'member/slack_up.html', {'form': form})

