from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
# Create your views here.


def index(request):
    return HttpResponse("<em>My Second App</em>")
    

def help(request):
    helpdict = {'insert_help': "Help Page"}
    return render(request, 'AppTwo/help.html', helpdict)

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'people': user_list}
    return render(request, 'AppTwo/users.html', user_dict)



