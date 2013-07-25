from django.conf.urls import patterns, include, url

from marks import views

urlpatterns = patterns(
    '',
    url(r'^$', views.list_marks),
    url(r'^add/$', views.add_mark),
    url(r'^delete/$', views.delete_mark),
    url(r'^register/$', views.register),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {
        'login_url': '/login'
    }),
)
