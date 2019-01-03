from django.conf.urls import url

from .views import home, view_post, view_category

urlpatterns = [
    url(r'home$', home, name='blog_home'),
    url(r'^blog/view/(?P<slug>[^\.]+)', view_post, name='view_blog_post'),
    url(r'^blog/category/(?P<slug>[^\.]+)', view_category, name='view_blog_category'),

]