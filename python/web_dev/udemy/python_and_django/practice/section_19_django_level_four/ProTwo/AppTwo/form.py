from django import forms
from AppTwo.models import User

## Save user data by connecting to ModelForm
##
class NewUserForm(forms.ModelForm):
    ##custom validations here
    ##first_name = forms.Char
    
    ##Meta class
    ##
    class Meta():
        model = User
        fields = '__all__'