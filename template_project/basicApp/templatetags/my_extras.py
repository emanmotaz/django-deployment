# custom templete filters
from django import template
register = template.Library()
#we can use decorators
# @register.filter(name=cut)
def cut(value,arg):
    """
    This cuts out all values of "arg" from string
    """
    return value.replace(arg,'')
# //register the filter
# register.filter('cut',cut) #we can use decorators
