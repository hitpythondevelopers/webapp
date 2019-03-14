from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SlackForm(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=254)

    def clean(self):
        cleaned_data = super(SlackForm, self).clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        if not username and not email:
            raise forms.ValidationError('You have to write something!')

    