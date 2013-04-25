from django.conf.urls import patterns, url

urlpatterns = patterns('Blog.views',
                       url(r'^article/(?P<id_article>\d+)-(?P<slug>.+)$', 'view_article'),
                       url(r'^category/(?P<id_category>\d+)-(?P<slug>.+)$', 'view_category'),
                       url(r'^archive/$', 'view_archive'),
                       url(r'^get_comment/(?P<id_article>\d+)$', 'get_comment'),
)
