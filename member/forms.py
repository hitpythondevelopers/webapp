from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper



class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password' )

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        name = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if not name and not email and not password:
            raise forms.ValidationError('Please fill in all the fields!')


    