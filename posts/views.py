from django.shortcuts import render
from .models import Post

def posts_list(request):
    # return HttpResponse('hello world, this is the homepage')
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})
