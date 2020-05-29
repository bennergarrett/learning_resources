from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

##make sure names are different
##
class UserCreateForm(UserCreationForm):
    
    class Meta:
        ##fields come from auth model
        ##
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        ##setting up customization label for form
        ##
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
        