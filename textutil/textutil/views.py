# i have created this website mukhtar
from django.http import HttpResponse
from django.shortcuts import  render
##def index(request):
    ##eturn HttpResponse("<a href='https://www.reddit.com/r/django/comments/lzg8ns/python_views_code_not_updating_in_server/'>mukhtar</a>")
def index(request):
    params={'name':'mukhtar' ,'place':'naptune'}
    return render(request,'index.html',params)
def removepunc(request):
    text=request.GET.get('text1')
    text = capitilize(text)
    print(text)
    return HttpResponse(text)
def capitilize(request):
    text =request.GET.get('text1')
    text=capitilize(text)
    print(text)

    return HttpResponse(text)
def charCount(request):

    return HttpResponse("charCount")
def SpaceRemover(request):
    return HttpResponse("spaceremove")