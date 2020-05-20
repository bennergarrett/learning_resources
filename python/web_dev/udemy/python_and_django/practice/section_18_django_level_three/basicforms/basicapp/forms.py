from django import forms

##importing django validators
##
from django.core import validators

##create own validator using django
##needs input to be value
##
def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("NAME NEEDS TO START WITH Z")

class FormName(forms.Form):
    name =          forms.CharField()
    email =         forms.EmailField()
    verify_email =  forms.EmailField(label='Enter your email again')
    text =          forms.CharField(widget=forms.Textarea)
    
    ##clean whole form
    ##
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        
        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")



    ##checks for bots
    ##
    # botcatcher = forms.CharField(required=False,
    #                              widget=forms.HiddenInput,
    #                              validators=[validators.MaxLengthValidator(0)])
    
    ##example to manually create valid data checks
    ##
    # ##custom validator using default method
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
        
    #     ##if bot scraped page
    #     ##
    #     if len(botcatcher):
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher