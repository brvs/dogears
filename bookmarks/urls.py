from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse

urlpatterns = patterns(
    '',
    url(r'^$', 'bookmarks.views.index', name='index'),
    url(r'^bookmarks/add/$', 'bookmarks.views.bookmark_add', name='add'),
    url(r'^bookmarks/delete/$', 'bookmarks.views.bookmark_delete', name='delete'),
    url(r'^bookmarks/visit/(?P<bookmark_id>\d+)$', 'bookmarks.views.bookmark_visit',
        name='visit'),
    url(r'^accounts/register/$', 'bookmarks.views.register_user', name='register'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login', {
        'login_url': '/accounts/login',
    }, name='logout'),
)
