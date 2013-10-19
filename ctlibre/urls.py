from django.conf import settings
from django.conf.urls import patterns, include, url, static
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'ctlibre.views.home', name='home'),
    url(r'^article/(?P<slug>[^/]+)', 'news.views.article_detail',
        name='article-detail'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

# Serve static media during development
urlpatterns += static.static(settings.MEDIA_URL,
                             document_root=settings.MEDIA_ROOT)
