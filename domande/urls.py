from django.conf.urls.defaults import url

from urls_sugar.utils import patterns, url_sugar


urlpatterns = patterns('domande.views',
    url(r'^$', 'index', name='index'),
)
