from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from . import forms

def posts_list(request):
    # return HttpResponse('hello world, this is the homepage')
    posts = Post.objects.filter(author=request.user).order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})

def post_page(request, slug):
    # post = Post.objects.get(slug=slug)
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'posts/posts_page.html', {'post': post})

@login_required(login_url="/users/login/")
def post_new(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES) 
        if form.is_valid():
            # save with user 
            newpost = form.save(commit=False) 
            newpost.author = request.user   
            newpost.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_new.html', { 'form': form }) 


@login_required(login_url="/users/login/")
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)

    # Check if the logged-in user is the owner of the post
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")
    
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:page', slug=post.slug)
    else:
        form = forms.CreatePost(instance=post)

    return render(request, 'posts/post_edit.html', {'form': form, 'post': post})

@login_required(login_url="/users/login/")
def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)

    # Check if the logged-in user is the owner of the post
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")
    
    # Delete the post
    post.delete()
    return redirect('posts:list')