from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
#from .member import views as member_views


from .views import home, portfolio, signup

urlpatterns = [
    url(r'^home/', home, name='member_home'),
    url(r'^login/', LoginView.as_view(template_name='member/login.html'), name='member_login'),
    url(r'^logout/', LogoutView.as_view(), name='member_logout'),
    url(r'^signup/', signup, name='member_signup'),
    url(r'^portfolio/', portfolio, name='member_portfolio'),
   

]