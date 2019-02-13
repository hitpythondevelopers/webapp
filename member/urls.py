from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
#from .member import views as member_views


from .views import slack_up

urlpatterns = [
    url(r'^slack/', slack_up, name='member_slack'),

]