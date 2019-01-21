from django.conf.urls import url
from .views import welcome, about_us, emailView, successView


urlpatterns = [
    url(r'^$', welcome, name='welcome'),
    url(r'about$', about_us, name='website_about'),
    url(r'email$', emailView, name='website_contact'),
    url(r'success$', successView, name='success'),
]