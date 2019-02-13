from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper



class SlackForm():
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ( 'email',)

    def clean(self):
        cleaned_data = super(SlackForm, self).clean()
        email = cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Please enter your email in the field provided!')


    