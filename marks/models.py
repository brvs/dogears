
import html

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

from marks.utils import webpage_data


class Bookmark(models.Model):
    user = models.ForeignKey(User)
    url = models.URLField()
    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now=True)
    last_accessed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @classmethod
    def create(cls, user, url):
        url = ('http://' if url[:7] != 'http://' and url[:8] != 'https://'
               else '') + url
        pagedata = webpage_data(url)
        title = (webpage_data(url).get('title') or url) if pagedata else url
        return cls(user=user, url=url, title=title)

    class Meta:
        ordering = ['-date_created']


class BookmarkForm(ModelForm):
    class Meta:
        model = Bookmark
        exclude = ('user', 'title')

