from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'trivia.views.home', name='home'),
    url(r'^q/$', 'trivia.views.perguntas', name='perguntas'),
    url(r'^r/$', 'trivia.views.reset', name='reset'),
    url(r'^sucesso/$', 'trivia.views.sucesso', name='sucesso'),
    url(r'^pena/$', 'trivia.views.falhou', name='falhou'),
)
