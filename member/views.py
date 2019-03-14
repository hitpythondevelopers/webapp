from django.shortcuts import render, redirect
from django.http import HttpResponse,  HttpResponseRedirect
from django.core.mail import send_mail,BadHeaderError
from django.template.loader import render_to_string, get_template
from django.shortcuts import render, redirect
from .forms import SlackForm


def slack_up(request):
    if request.method == 'GET':
        form = SlackForm()
    elif request.method == 'POST':
        form = SlackForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            message = "{0} has sent you a new message:\n\n{1}".format(username, email)

            try:
                send_mail('New Member Request', message, email, ['hitpythondevelopers@gmail.com'])
                return redirect('index.html')

            except BadHeaderError:
                return HttpResponse('Invalid header found.')   
    return render(request, "signup.html", {'form': form})


            
