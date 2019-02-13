from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView


from .views import slack_up, success

urlpatterns = [
    url(r'^slack/', slack_up, name='member_slack'),
    url(r'^success/',success, name='success'),

]