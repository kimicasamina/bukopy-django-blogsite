from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

def posts_list(request):
    # return HttpResponse('hello world, this is the homepage')
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/posts_page.html', {'post': post})
