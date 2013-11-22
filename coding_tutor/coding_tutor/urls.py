from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'coding_tutor.views.home', name='home'),
    # url(r'^coding_tutor/', include('coding_tutor.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
