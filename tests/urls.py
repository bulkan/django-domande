from django.conf.urls import url, patterns

urlpatterns = patterns('tests.views',
    url(r'^$', 'index', name='index'),
)
