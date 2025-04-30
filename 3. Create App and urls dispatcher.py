# What is an App?
# 🫡 An app is Web Application use to create different task like website app for complete Website as Home Page, About Us Page, Contact Us Page, etc, a contact form, or website blog, or any other application which you want to run seperately. 

# Minimum 1 app you need to create to run web application✅

# Create App (Module) in your Project:✅
# Will give name to app as website

✅# In the Terminal type:
      py manage.py startapp application

# Project1
    # manage.py
    # Project1/
    # application/
    #     migrations/
    #         __init__.py  
    #     __init__.py
    #     admin.py
    #     apps.py
    #     models.py
    #     tests.py
    #     views.py

# as soon as we create app, we need to register that app, in default app settings.py file 

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'application.apps.ApplicationConfig',👍
]

# 'application.apps.ApplicationConfig',   - We need to register new created app application in settings.py file which is available in default app  🫡

# Note : Remember one thing you need to create urls.py file in the same Home app as MVT Architecture says through urls.py only it will moves to views.py and then model(if form or table required) and template (UI Design)

# Therefore Compulsory create urls.py file in your newly created app and from urls page redirect to views.py page where functions are available for redirect path.👍

# When we create Project, default project name one default app is created, where settings.py👍
# file is available, which is the Project Setting file, all project related settings you need to write in this settings.py file

# Copy urls.py from default project app and create in Home app which is our new app we created in Project

from django.contrib import admin✅
from django.urls import path, include✅

admin.site.site_header = "Elite Softwares Admin"
admin.site.site_title = "Elite Softwares Admin Portal"
admin.site.index_title = "Welcome to Elite Softwares Portal"

# Above three lines for to change admin login page Heading Change✅

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('application.urls')),
]

# As we are using include() therefore include module we need to import✅

path('', include('application.urls'))

# Above path() meaning when blank path got from browser example - www.abc.com - then it should be redirect to Home.urls page
# Home (is our created app)

# then it redirects to Home apps urls.py file and then that urls.py file decide which views should be call

# Once urls.py file is calling from Home app then we need to redirect to views.py as:✅

from django.contrib import admin
from django.urls import path
from application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name ='home'),
    path('contactus', views.contactus, name ='contactus'),
        
]
contactus/'  IS PATH NAME
views.contactus/ function calling
contactus/ techinal name  for hyperlink {click kar ro or page ko open kar ro }




















