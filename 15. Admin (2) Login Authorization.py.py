# https://docs.djangoproject.com/en/4.0/topics/auth/default/#auth-web-requests

# Find this doc for django authentication for web request

from django.shortcuts import redirect, render 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# import above module in views.py file to autheticate login

# import one more module as messages() as we are using for display messages to user information sent or not...


def login_user(request):
    if request.method == "POST":
        a = request.POST['username']
        b = request.POST['password']
        
        user = authenticate(request, username = a, password = b)

        if user is not None:
            # is not None is keyword None 'N' is capital which check above user (username and password) is available in database or not
            # is is a indity operator 
            login(request, user)
            # Redirect to a success page.
            return redirect('dashboard')
            # redirect('dashboard') - dashboard is a technical name not a path name, give technical name of that function from where dashboard.html page will render
            
            # from django.shortcuts import redirect, render - this module we need to import in same file, to access redirect() where only path name should be call
        else:
            # display 'invalid login' error message
            messages.error(request, 'In-correct username or password!..')    
        
    return render(request, 'login.html')


# Remember for login authorization no need to create model
# as from super admin we can create admin user and using login authorization we can login to dashboard for admin view
