from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper



class SlackForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=254)

    def __init__(self, *args, **kwargs):
        super(SlackForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Your name:"
        self.fields['email'].label = "Your email:"

    