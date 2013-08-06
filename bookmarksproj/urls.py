from django.conf.urls import patterns, include, url
from django.contrib import admin

import bookmarks.urls
from bookmarks.models import Bookmark

admin.autodiscover()
admin.site.register(Bookmark)

urlpatterns = patterns(
    '',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(bookmarks.urls))
)
