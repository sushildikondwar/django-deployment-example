from django import template

# template.Library is the built-in function which is used to Register our custom filters
register = template.Library()    # 'L' is in Upper Case

def cutoff(value,arg):      # VALUE = PREVIOUS VALUE INPUT i.e., the value before the PIPE Operator
    """
    THIS CUTS OUT ALL VALUES OF ARG FROM THE STRING(VALUE)
    """
    return value.replace(arg,'')

register.filter('cut',cutoff)    # 'cut' is the string which we will use to call the function cutoff
                                              # from myextras.py as a custom filter
