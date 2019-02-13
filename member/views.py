from django.shortcuts import render, redirect
from django.http import HttpResponse,  HttpResponseRedirect
from django.core.mail import send_mail,BadHeaderError
from django.template.loader import render_to_string, get_template
from django.shortcuts import render, redirect
from .forms import SlackForm

def success(request):
    return render(request, 'member/success.html')


def slack_up(request):
    if request.method == 'GET':
        form = SlackForm
    else:
        form = SlackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = "{0} has sent you a new message:\n\n{1}".format(name, email)

            try:
                send_mail('New Member Request', message, email, ['hitpythondevelopers@gmail.com'])
                return redirect('member/success.html')

            except BadHeaderError:
                return HttpResponse('Invalid header found.')   
    return render(request, "member/slack_up.html", {'form': form})


            
    