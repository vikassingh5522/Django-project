# Restrict Anonymous User from accessing pages through Browser URL:

# Suppose anonymous user knows your path name (page name) example dashboard path name where enquiry details are available

# Only database user can access enquiry details or database information not to anonymous user.

# For that purpose we need to use python-django in-built decorators:

Python Decorators:

# In Python, a decorator is a function that takes another function as an argument and adds functionality or augments (adding to it) the function without changing it. Django, as a Python web framework, comes with a large number of built-in decorators. These built-in decorators are used when decorating function-based views.

# so to prevent accessing dashboard page we need to import one module in views.py where execution logic we write.

from django.contrib.auth.decorators import login_required

# Above module we need to import in views.py file

Now to which function() (means which page) you want to restrict from anonymous user (as we call .html page from function), just above to that you need to call @login_required in-built function of Decorators 


# To anonymous user we are redirecting to login page, because now dashboard function enable for login_required condition
@login_required(login_url='login')
def dashboard(request):
    info = enquiry_table.objects.all()
    # enquiry_table is table name which we create in models.py
    
    data = {'information':info}
    return render(request, 'dashboard.html',data)








