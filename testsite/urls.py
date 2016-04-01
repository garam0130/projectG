from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls', namespace= 'accounts')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^', include('blog.urls', namespace='blog'))
]


if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{
            'document_root': settings.MEDIA_ROOT,
            }
        ),
    ]