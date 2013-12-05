from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'artwark.views.home', name='artwark_home'),
    url(r'^r/$', 'artwark.views.reset', name='artwark_reset'),
    url(r'^acabou/$', 'artwark.views.acabou', name='artwark_acabou'),
    url(r'^maximo/$', 'artwark.views.maximo', name='artwark_maximo'),
    url(r'^assinar/$', 'artwark.views.assinar', name='artwark_assinar'),
    url(r'^agradecimento/$', 'artwark.views.agradecimento', name='artwark_agradecimento'),
    url(r'^proxima/$', 'artwark.views.proxima', name='artwark_proxima'),
)
