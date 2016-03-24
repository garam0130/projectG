from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^travel/$', views.travel, name='travel'),
    url(r'^travel/(?P<value>[0-9]{4})/$', views.year, name='year'),
]