from django.conf.urls import patterns, include, url

from marks import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index),
    url(r'^bookmarks/add/$', views.bookmark_add),
    url(r'^bookmarks/delete/$', views.bookmark_delete),
    url(r'^accounts/register/$', views.register_user),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login', {
        'login_url': '/login'
    }),
)
