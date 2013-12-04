from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'trivia.views.home', name='home'),
    url(r'^q/$', 'trivia.views.perguntas', name='perguntas'),
    url(r'^r/$', 'trivia.views.reset', name='reset'),
)
