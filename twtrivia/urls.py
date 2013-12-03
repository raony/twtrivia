from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'twtrivia.views.home', name='home'),
    url(r'^trivia/', include('trivia.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
