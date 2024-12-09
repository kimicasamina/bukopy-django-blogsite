from django.http import HttpResponse

def homepage(request):
    return HttpResponse('hello world, this is the homepage')

def about(request):
    return HttpResponse('My about page')