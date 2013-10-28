from django.conf import settings
from django.conf.urls import patterns, include, url, static
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'ctlibre.views.home', name='home'),
    url(r'^article/(?P<slug>[^/]+)', 'news.views.article_detail',
        name='article-detail'),
    url(r'^admin/', include(admin.site.urls)),
)

# Serve static media during development
urlpatterns += static.static(settings.MEDIA_URL,
                             document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('',
    url(r'^', include('cms.urls')),
)
