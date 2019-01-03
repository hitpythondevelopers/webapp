from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'', include('website.urls')),
    url(r'^member/', include('member.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/', include('django_registration.backends.activation.urls')),
    

]