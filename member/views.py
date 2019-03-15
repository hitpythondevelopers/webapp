from django.shortcuts import render, redirect
from django.http import HttpResponse,  HttpResponseRedirect
from django.core.mail import send_mail,BadHeaderError, EmailMessage
from django.template.loader import render_to_string, get_template
from django.shortcuts import render, redirect
from .forms import SlackForm


def slack_up(request):
    if request.method == 'GET':
        form = SlackForm()
    else:
        form = SlackForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            message = "{0} has sent you a new message:\n\n{1}".format(username, email)

            try:
                email = EmailMessage(username, message, email, ['hitpythondevelopers@gmail.com'], reply_to=[email])
                email.send()
                
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('index.html')   
    return render(request, "signup.html", {'form': form})


            
