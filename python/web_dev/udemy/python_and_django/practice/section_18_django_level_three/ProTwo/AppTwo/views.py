from django.shortcuts import render
#from django.http import HttpResponse
#from AppTwo.models import User
from AppTwo.form import NewUserForm
# Create your views here.


def index(request):
    return render(request, 'AppTwo/index.html')
    

def help(request):
    helpdict = {'insert_help': "Help Page"}
    return render(request, 'AppTwo/help.html', helpdict)

def users(request):
    form = NewUserForm()
    
    ##if someone hits submit
    ##request to post
    ##check if valid
    ##
    if request.method == "POST":
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            form.save(commit = True)
            
            ##return to index page
            ##
            return index(request)
        
        else:
            print('ERROR FORM INVALID')
    
    return render(request, 'AppTwo/users.html', {'form':form})
    
        
        



