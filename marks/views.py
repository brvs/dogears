
from django.contrib.auth import authenticate, forms, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render

from marks.models import Bookmark, BookmarkForm


@login_required
def list_marks(request, bookmark=None):
    return render(request, 'marks/index.html', {
        'bookmarks': Bookmark.objects.filter(user=request.user),
        'bookmark_form': BookmarkForm(instance=bookmark)
    })


def add_mark(request):
    url = None
    redir = None
    post = False

    if request.method == 'POST':
        url = request.POST['url']
        redir = '/'
        post = True
    elif request.method == 'GET':
        url = request.GET['url']
        redir = request.GET['return']
    #TODO consider other request methods
    
    bookmark = Bookmark.create(request.user, url)

    try:
        bookmark.full_clean()
        bookmark.save()
        return HttpResponseRedirect(redir)
    except ValidationError as e:
        return list_marks(request, bookmark) if post else render(
            request, 'marks/bookmarklet_failure.html', { 'redir': redir })


def delete_mark(request):
    # TODO allow undo
    if request.method == 'POST':
        Bookmark.objects.get(pk=request.POST['id']).delete()
        return HttpResponseRedirect("/")        


def register(request):
    form = None
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/')
    else:
        form = forms.UserCreationForm()
        
    return render(request, 'registration/register.html', {
        'form': form
    })


