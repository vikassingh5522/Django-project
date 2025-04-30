# DJango Project Deployment on server through cpanel

# Once our DJango project completed or you want to upload django project on server through cpanel, few steps we need to perform then only it will display online browser

step 1) login to cpanel, if you want to upload your project on sub domain name, then create sub domain using cpanel or you can upload to main domain also.

step 2) cPanel dashboard find: 
# SETUP PYTHON APP, here we need to setup python application, (If not available in cpanel, then you need to talk to hosting provider to enable this setup python app module)


step 3) Click to CREATE APPLICATION button -> 

#    select Python Version :(Any version you can select latest one you can select) 
# -> then under Application Root : text box write your DJango Project Name e.g. Project_Name 

# -> then under Application URL : select sub domain name or domain name where you want to show Django project

# -> then Application startup file and Application Entry point these 2 text box leave blank (no need to fill) 

# -> then Passenger log file : Project_Name/passenger.log
# (You can define the path along with the filename) (e.g. /home/elitesoftwares/Project_Name/passenger.log)

# This log file maintain activities of our project, useful for debugging errors, in case crash application insides we can get from this log file. 

# -> and then finally click to CREATE Button. - it will take some time to create application and then message will show, Python Application Created.


step 4) Now you can check, outside public_html folder, you will get folde of Project_Name which you create from setup python application, 

Upload your DJango project ( zip folder upload and then unzip ) in this folder not in sub domain name.

# step 5 ) Once unzip, move all files and folders of un-zip folder into project_name (means default_app, custom app and other files) which is available outside public_html folder. 

step 6) Now virtual environment command we get from cpanel, 
# Go to setup python app -> click to edit and you will get path (just click to link it will auto copy) : source /home/elitesoftwares/virtualenv/Project_Final/3.8/bin/activate && cd /home/elitesoftwares/Project_Name

# In this virtual environment we need to install libraries link pip install django, etc all required libraries

# When we create application and virtual environment, now you can see sub domain on browser you will get as : 
  It Works! Python 3.8.16 (version which you select)

This message comes from our Django project folder there is one file auto create which is passenger_wsgi.py from this file message showing means all working fine.

# Now you can see Application startup file and Application Entry point with file name and appliaction as name, this comes auto when we create application therefore we keep blank before.


# step 6) But we don't want to show It works message on browser, we want to display our DJango Project right, therefore we need to change passenger.wsgi.py file which is our Application startup file and this file available in the root directory outside public_html folder,

# You can see project_name folder is created and in that you will get passenger.wsgi.py file,
# open this file and point to our project default page rather than It Work's message.

import os
import sys

# Do not comment import os and import sys

# sys.path.insert(0, os.path.dirname(__file__))


# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/plain')])
#     message = 'It works!\n'
#     version = 'Python %s\n' % sys.version.split()[0]
#     response = '\n'.join([message, version])
#     return [response.encode()]

# Above from sys.path to return we need to comment code from passenger.wsgi.py file and add one line as:

from write_your_Default_App_Name.wsgi import application

# Note : Project_Final is Default app which is inside project name,
# it means under default app there is one file wsgi.py go inside that file and read application function and run on browser


# step 7) Now we need to configure virtual environment using terminal into cpanel as we get from cpanel, just copy that link and paste into terminal of cpanel (not in local pc ternimal) - paste link after $ sign

# as : [elitesoftwares@52-66-221-45 ~] $ source /home/elitesoftwares/virtualenv/Project_Final/3.8/bin/activate && cd /home/elitesoftwares/Project_Final

# (Note: if terminal not available in your cpanel, again you need to call to hosting provider and enable terminal service in your cpanel dashboard.)

# Now virtual environment is created in cpanel, now you can install django using pip command as: [elitesoftwares@52-66-221-45 ~] $ pip install django

((Project/Final:3.8)) [elitesoftwares@52-66-221-45 Project_Final]$ pip install django
Collecting django
  Downloading Django-4.2-py3-none-any.whl (8.0 MB)
     |████████████████████████████████| 8.0 MB 2.8 kB/s
Collecting sqlparse>=0.3.1
  Downloading sqlparse-0.4.4-py3-none-any.whl (41 kB)
     |████████████████████████████████| 41 kB 433 kB/s
Collecting asgiref<4,>=3.6.0
  Downloading asgiref-3.6.0-py3-none-any.whl (23 kB)
Collecting backports.zoneinfo
  Downloading backports.zoneinfo-0.2.1-cp38-cp38-manylinux1_x86_64.whl (74 kB)
     |████████████████████████████████| 74 kB 6.4 MB/s
Installing collected packages: sqlparse, backports.zoneinfo, asgiref, django
Successfully installed asgiref-3.6.0 backports.zoneinfo-0.2.1 django-4.2 sqlparse-0.4.4
WARNING: You are using pip version 21.3.1; however, version 23.1.2 is available.
You should consider upgrading via the '/home/elitesoftwares/virtualenv/Project_Final/3.8/bin/python3.8_bin -m pip install --upgrade pip' command.
((Project/Final:3.8)) [elitesoftwares@52-66-221-45 Project_Final]$


# This way your django framework will install in your particular that project.


# step 8) Now open default app -> settings.py file, from where we unzip project, open that project and go to default app settings.py and in 
ALLOWED_HOSTS = ['project1.elitesoftwares.in']

# (Enter sub domain name or domain name means we are giving permission to allow project on this domain)


# and now finally go back to setup python app in cpanel and click to restart icon and check browser.


# step 9) Now again in terminal, run : pip install mysqlclient (if you are using mysql database),
#pip install djangorestframework (if rest api you are created in your project) and 

# step 10) Now Project Images will not display on browser, because project is running from root directory and url is different therefore in url on sub domain name path we need to copy and paste static folder, then only images will display.

Now you have to create database online in cpanel to access tables records and admin login.



