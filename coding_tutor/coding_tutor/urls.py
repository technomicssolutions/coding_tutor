from django.conf.urls import patterns, include, url

from django.contrib import admin
from web.views import (Home,SignUp)
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'coding_tutor.views.home', name='home'),
    # url(r'^coding_tutor/', include('coding_tutor.foo.urls')),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^register/$', SignUp.as_view(), name='signup'),
    url(r'^admin/', include(admin.site.urls)),
    


)
