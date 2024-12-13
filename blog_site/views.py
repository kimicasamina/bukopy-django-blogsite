# from django.http import HttpResponse
from django.shortcuts import render 
from posts.models import Post 


def homepage(request):
    # return HttpResponse('hello world, this is the homepage')
    posts = Post.objects.all().order_by('-date')
    return render(request, 'home.html', { 'posts': posts })

def about(request):
    # return HttpResponse('My about page')
    return render(request, 'about.html')