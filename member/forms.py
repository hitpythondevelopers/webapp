from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SlackForm(forms.Form):
    username = forms.CharField(required=True, label="Username")
    email = forms.EmailField(required=True, label="Email")

    