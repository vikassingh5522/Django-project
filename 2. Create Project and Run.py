# Creating project of name First_Project using terminal:


django-admin startproject Project_name

# if showing "django-admin" not recognized internal or external command - error
# then we need to run below command:✅

1} home or

2} py -m django startproject Project_Name  or

3} python3 -m django startproject Project_Name

# Note : underscore _ is allowed in Project Name as Prject_MIT✅

# Note : Project Name does not allowed : spaces as Project College, - as Project-College, digits before name as 123Project not allowed✅


# Project1🧑‍💻
    # manage.py
    # Project1/
    #     __init__.py
    #     asgi.py
    #     settings.py
    #     urls.py
    #     wsgi.py

# These are default files and folder which created by django framework



# Run the Django Project on Browser before that you need to enter in that project Name using:👍
# On Terminal type : 

                 😎cd Project_Name

# and then you can run project

# On Terminal type 
👍python manage.py runserver
or
👍py manage.py runserver
or
👍python3 manage.py runserver

# Python excute and start server and gives you ip address to see output✅

# System check identified no issues (0 silenced).
# ←[31m
# You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.←[0m
# ←[31mRun 'python manage.py migrate' to apply them.←[0m
# May 30, 2022 - 15:23:54
# Django version 3.2.13, using settings 'First_Project.settings'

# Starting development server at 
  http://127.0.0.1:8000/

# Quit (stop) the server with CTRL-C. 👍


# default project name app is created where settings.py file available and urls.py also

# Now look MVT Architecture - request first goes to URL then -> Views then -> Templates (Design)

# Now Open default app urls.py file, where you can see if it is blank path by user then there is NO Home.urls (Home is app name - case sensitive) calling and therefore we need to call Home.urls and that page name as:

# we need to import include module and then use in urls.py file of default app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
]

# and now you can create app with name Home and in that Home app create urls.py and copy default app urls.py into urls.py of Home app (which you create)


How to change project name after create project using command:

First Rename Project Name and Default app name which you want New Project Name then

In 3 Files you need to change New Project Name as:
✅1) Settings.py file - 
ROOT_URLCONF = 'Project_Name.urls'  - which you rename project name enter that name here replace to Project_Name

🤷‍♂️(web server gateway interface )WSGI_APPLICATION = 'Project_Name.wsgi.application'

✅2) wsgi.py file - 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_Name.settings')


✅3) asgi.py file -
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_Name.settings')

✅4) manage.py file -
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_Name.settings')























