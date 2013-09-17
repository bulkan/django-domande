from django.conf.urls import url, patterns


urlpatterns = patterns('domande.views',
    url(r'^$', 'index', name='index'),
)
