from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView


from .views import home

urlpatterns = [
    url(r'^home/',home, name='blog_home'),

]