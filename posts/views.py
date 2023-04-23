import json

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseNotFound

from posts.models import Post, Comment

from rest_framework import status


@login_required
def home(request):
    return render(request, 'posts/home.html', {
        'posts': Post.objects.all().order_by('-created_at')
    })


@login_required
def posts(request):
    method = request.method
    if method == 'POST':
        if not request.user.has_perm('posts.add_comment'):
            return HttpResponse(status=status.HTTP_403_FORBIDDEN)

        data = request.POST.dict()
        title, content = data.get('title', ''), data.get('content', '')
        try:
            post = Post.objects.create(title=title, content=content, author_id=request.user.id)
            return HttpResponse(json.dumps({'id': post.id}), status=status.HTTP_201_CREATED)
        except:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    return HttpResponseNotFound()


@login_required
@permission_required('posts.view_post', raise_exception=True)
def post_details(request: HttpRequest, id: int):
    method = request.method
    if method == 'POST':
        if not request.user.has_perm('posts.add_post'):
            return HttpResponse(status=status.HTTP_403_FORBIDDEN)

        data = request.POST.dict()
        content = data.get('content', '')

        try:
            post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

        comment = Comment.objects.create(content=content, post=post, author_id=request.user.id)
        return HttpResponse(json.dumps({'id': comment.id}), status=status.HTTP_201_CREATED)
    else:
        post = get_object_or_404(Post, id=id)
        return render(request, 'posts/post_details.html', {
            'post': post,
            'comments': Comment.objects.filter(post__id=id)
        })


@login_required
@permission_required('posts.add_post', raise_exception=True)
def post_create(request):
    return render(request, 'posts/create_post.html')
