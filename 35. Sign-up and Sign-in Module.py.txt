
Sign-up and Sign-in Module:

as in every project or Portal, User sign-up and login is there, so in this topic we learn how we can maintain user sign-up and login module.

# Add one new Menu as Signup and already we have Login menu.

On click to sign-up menu, we required one form, from where user can fill form and sign-up to portal.

so we required to create new path, function and web page for signup page.

# In urls.py create path as:

path('signup/', views.signup, name='signup'),

# In views.py create function as:

def signup(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        surname = request.POST.get('surname')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')

        myuser = User.objects.create_user(username, email, password1)
        
        # Import below module in views.py to access User() function
        # User is a default table name where all users are stored, which admin user we create that also stored in User table

        # from django.contrib.auth.models import User
      
        myuser.first_name = first_name
        myuser.surname = surname

        myuser.save()

        messages.success(request, 'Congratulations, You are sign-up successfully, Now you can sign-in.. ')


    return render(request, 'dashboard/signup.html')

# and create one web page in Dashboard folder as signup.html where create form as:

 <form action="{% url 'signup' %}" method="POST" name="signup">
              <!-- In front of action="this name should be technical name of function using contact.html page is showing on the browser which we write in urls.py file as views.reg" -->
  
              {% csrf_token %}
      <!-- Cross-Site Request Forgery (CSRF) is an attack that forces authenticated users to submit a request to a Web application against which they are currently authenticated.
      CSRF Token used to prevent unathorized person could not submit form from your website-->
              <div class="form-group">
                <input type="text" class="form-control" placeholder="User Name" name="username" required>
              </div>
              <div class="form-group">
                <input type="text" class="form-control" placeholder="First Name" name="first_name" required>
              </div>
              <div class="form-group">
                <input type="text" class="form-control" placeholder="Surname Name" name="surname" required>
              </div>
              <div class="form-group">
                <input type="text" class="form-control" placeholder="Mobile Number" name="mobile" required>
              </div>
              <div class="form-group">
                <input type="email" class="form-control" placeholder="Your Email" name="email" required>
              </div>
              <div class="form-group">
                <input type="password" class="form-control" placeholder="Enter Your Password" name="password" required>
              </div>
              <div class="form-group">
                <input type="password" class="form-control" placeholder="Confirm Your Password" name="password2" required>
              </div>
              
              <div class="form-group">
                <input type="submit" value="Submit" class="btn btn-primary py-3 px-5" name="submit">
              </div>
            </form>


# Now you can login to DJango administration and check user is created after submit sign-up form.

login to superuser and check in Users table:
url : 127.0.0.1:8000/admin

# Now with new username and password will check, login working or not,

# and already login authorization work is done admin user create time, same login page we can use for sign-in also,

click to Login Menu and check with new username and password which we create from sign-up form, now you can see new user is logged In.


---- How we can fetch user name on dashboard page when user logged-In ----

as already username we save in varialble in function as:

        myuser = User.objects.create_user(username, email, password)
        myuser.username = username
        
        myuser.save()

# so myuser.username we can fetch on dashboard page after login to user.

In login authorization function we have to get session['username'] and send on dashboard/index.html page as:

def login_user(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username = username, password = password)

        if user is not None:
            
            login(request, user)
            request.session['username'] = username
            
            # Here under username varibale we stores username of portal and now we can fetch on dashboard.index.html page

            # Redirect to a success page.
            return redirect('dashboarddemo')
            

@login_required(login_url='login')
def dashboard(request):

    # print('Hi, the User Name is: ',request.session.get('username_id'))

    username = request.session.get('username')

    return render(request, 'dashboard/index.html', {'username':username})

# as now username we are sending on dashboard/index.html, through dictionary and finally we can show that user name on web page as:

                    <marquee direction="up" style="height:300px;" onmouseover="this.stop();" onmouseout="this.start();">

                        {% if user.is_authenticated %}
                
                          <h3> Hello, {{ username }}</h3>
    
                        {% endif %}
                        <br><br>
                        <b>Welcome to Freelancer House Wife Portal</b>

                    </marquee>


and Now you can check, which user logged-In that name will display on dashboard/index.html page in marquee as we fetch in marquee.





