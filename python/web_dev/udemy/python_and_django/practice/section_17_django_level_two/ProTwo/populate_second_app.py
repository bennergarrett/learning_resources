import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django

##Allows you to manipulate SQL server
##
django.setup()

import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        
        ## found out later it can be fakegen.name.firstName()
        ##
        first, last = fakegen.name().split(" ", 1)
        email_addr = fakegen.email()
        
        ## new entry
        ##
        full_user = User.objects.get_or_create(first_name = first, 
                                               last_name = last, 
                                               email = email_addr )[0]
        

if __name__ == '__main__':
    print("Populating data!")
    populate(10)
    print("Finished Populating!")