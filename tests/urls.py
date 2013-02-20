from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('domande.views',
    url(r'^$', 'index', name='index'),
)
