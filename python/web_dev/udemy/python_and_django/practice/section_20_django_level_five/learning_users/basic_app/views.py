from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

##create users
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'basic_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    

def register(request):
    
    ##default to false to check
    ##
    registered = False
    
    if request.method == "POST":
        user_form = UserForm(data= request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            
            user = user_form.save()
            
            ##hashes password
            ##
            user.set_password(user.password)
            user.save()
    
            ##commit false to avoid collisions
            ##
            profile = profile_form.save(commit=False)
            
            ##creates one to one relationship
            ##
            profile.user = user 
            
            ##check if picture submitted
            ##
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()
            
            registered = True
        
        ##invalid form
        ##
        else:
            print(user_form.errors, profile_form.errors)
          
    ##if not set to post
    ##
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        
    return render(request, 'basic_app/registration.html', 
                  {'user_form':user_form,
                   'profile_form':profile_form,
                   'registered':registered})
    
    

def user_login(request):
    if request.method == 'POST':
        ##used simple http on login.html
        ##
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        ##authenticates user in one line of code
        ##
        user = authenticate(username = username, password = password)
        
        if user:
            ##check if active user
            ##
            if user.is_active:
                login(request, user)
                ##redirect back to home page
                ##
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("someone tried to login and failed!")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("invalid login details supplied")
        
    else:
        return render(request, 'basic_app/login.html', {})



