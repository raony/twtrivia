from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'twtrivia.views.home', name='home'),
    url(r'^trivia/', include('trivia.urls')),
    url(r'^artwark/', include('artwark.urls')),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
