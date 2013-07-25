from django.conf.urls import patterns, include, url
from django.contrib import admin

import marks.urls
from marks.models import Bookmark

admin.autodiscover()
admin.site.register(Bookmark)

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'dogear.views.home', name='home'),
    # url(r'^dogear/', include('dogear.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(marks.urls))
)
