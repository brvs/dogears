
import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, forms, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render

from bookmarks.models import Bookmark, BookmarkForm


@login_required
def index(request, bookmark=None):
    if not request.method in ('GET', 'POST'):
        raise Http404
    return render(request, 'bookmarks/index.html', {
        'bookmarks': Bookmark.objects.filter(user=request.user),
        'bookmark_form': BookmarkForm(instance=bookmark)
    })


@login_required
def bookmark_add(request):
    url = None
    redir = None
    post = False

    if request.method == 'POST':
        url = request.POST.get('url')
        redir = reverse(index)
        post = True
    elif request.method == 'GET':
        url = redir = request.GET.get('url')
    else:
        raise Http404

    bookmark = Bookmark.create(request.user, url)

    try:
        bookmark.full_clean()
        bookmark.save()
        return HttpResponseRedirect(redir)
    except ValidationError as e:
        return list_marks(request, bookmark) if post else render(
            request, 'bookmarks/bookmarklet_failure.html', { 'redir': redir })


@login_required
def bookmark_delete(request):
    # TODO allow undo
    if request.method != 'POST':
        raise Http404
    Bookmark.objects.get(pk=request.POST['id'], user=request.user).delete()
    return HttpResponseRedirect(reverse(index))


@login_required
def bookmark_visit(request, bookmark_id):
    if request.method != 'GET':
        raise Http404
    bookmark = Bookmark.objects.get(pk=bookmark_id)
    bookmark.last_accessed = datetime.datetime.now()
    bookmark.save()
    return HttpResponseRedirect(bookmark.url)


def register_user(request):
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.INFO,
                'Registration successful. Please sign in with your new account.')
            return HttpResponseRedirect(reverse(index))
    elif request.method == 'GET':
        form = forms.UserCreationForm()
    else:
        raise Http404

    return render(request, 'registration/register.html', {
        'form': form
    })
