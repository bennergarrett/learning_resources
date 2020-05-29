from django.db import models
##user models
##
from django.contrib import auth

# Create your models here.


class User(auth.models.User, auth.models.PermissionsMixin):
    
    
    def __str__(self):
        
        ##username defiend with .User
        ##
        return "@{}".format(self.username)