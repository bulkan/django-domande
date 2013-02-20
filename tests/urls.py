from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('tests.views',
    url(r'^$', 'index', name='index'),
)
