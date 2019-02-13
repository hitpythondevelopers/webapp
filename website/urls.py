from django.conf.urls import url
from .views import welcome, about_us

urlpatterns = [
    url(r'^$', welcome, name='welcome'),
    url(r'about$', about_us, name='website_about'),
]