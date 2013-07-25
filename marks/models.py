from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


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
        # TODO: Grab title from page
        return cls(user=user, url=url, title=url)


class BookmarkForm(ModelForm):
    class Meta:
        model = Bookmark
        exclude = ('user', 'title')

