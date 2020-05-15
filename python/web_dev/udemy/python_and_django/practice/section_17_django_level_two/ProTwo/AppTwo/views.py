from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<em>My Second App</em>")

def help(request):
    helpdict = {'insert_help': "Help Page"}
    return render(request, 'AppTwo/help.html', helpdict)
