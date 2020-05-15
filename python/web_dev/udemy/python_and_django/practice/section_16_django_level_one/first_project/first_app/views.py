from django.shortcuts import render
##added
##
from django.http import HttpResponse

# Create your views here.

##added code
##created view called index
##by convention input called request
##
def index(request):
    ##must return http model
    ##
    ##return HttpResponse("Hello World!")
    my_dict = {'insert_me': "Hello I am from views.py I am coming from first_app/index.html!"}
    return render(request, 'first_app/index.html', my_dict)

def help(request):
    my_dict = {'insert_help': "Help Page"}
    return render(request, 'first_app/help.html', my_dict)
