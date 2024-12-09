from django.shortcuts import render

def posts_list(request):
    # return HttpResponse('hello world, this is the homepage')
    return render(request, 'posts/posts_list.html')
