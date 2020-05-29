##django custom template tags
##
from django import template

register = template.Library()

##write function
##and register
##
@register.filter(name='cutter')
def cutter(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

##decorator does this
#register.filter('cutter', cutter)