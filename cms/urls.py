from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('cms.views',
    url(r'(?P<slug>[^/]+)/?', 'main', name='cms'),
)
