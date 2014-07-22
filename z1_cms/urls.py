from django.conf.urls import patterns, url
from z1_cms.views import index_rss
from z1_cms import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^category$', views.category_list, name='types'),
    url(r'^category/(?P<category_id>\d+)$', views.entity_list, name='category'),
    url(r'^entity/(?P<entity_id>\d+)$', views.entity, name='entity'),
    url(r'^rss$', index_rss(), name='index_rss'),
)
