
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse


def context(request):
    site = Site.objects.get_current(),
    return {
        'site': site[0],
        'bookmarklet': ''.join([ "javascript:window.location='http://",
                                 site[0].domain, reverse('add'),
                                 "?url='+window.location" ])
    }
