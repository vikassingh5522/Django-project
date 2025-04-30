
DJango REST API Framework: (DRF)  ✅✔️

# Django REST framework is a powerful and flexible toolkit for building Web APIs. Some reasons you might want to use REST framework: The Web browsable API is a huge usability win for your developers.

# Main advantages of Django REST framework: Simplicity, flexibility, quality, and test coverage of source code. 

# Authentication policies including packages for OAuth1a and OAuth2

# Powerful serialization engine compatible with both ORM (Object Relational Mapping) and non-ORM data sources. Pluggable and easy to customise emitters, parsers, validators and authenticators.

CRUD Operations - Create, Read, Update and Delete Operatios

Operation       HTTP Method       Description

1) Create       POST()            Creating/Posting/Inserting Data 

2) Read         GET()             Reading/getting/Retrieving Data

3) update       PUT(), PATCH()    Updating Data: 
                                  PUT() - Complete Update
                                  PATCH() - Partial Update

4) Delete       DELETE()          Deleting Data


API resource :

https://abc.com/api/studentprofile

1) https://abc.com/ - Base URL 💡

2) /api/ - Naming Convention 💡

3) /studentprofile - Resource of API or End-Point 💡


How to Install Django Rest Framework - (DRF) ✅

pip install djangorestframework 

# above command type in terminal (command propmt) and we can easily install django rest framework in our system

# once you run installing command, below installing steps will show with message at the end as Successfully installed djangorestframework-3.14.0


C:\Users\admin\Desktop\DJango Programs> pip install djangorestframework
Collecting djangorestframework
  Downloading djangorestframework-3.14.0-py3-none-any.whl (1.1 MB)
     |████████████████████████████████| 1.1 MB 939 kB/s
Requirement already satisfied: pytz in c:\users\admin\appdata\local\programs\python\python36-32\lib\site-packages (from djangorestframework) (2022.1)
Requirement already satisfied: django>=3.0 in c:\users\admin\appdata\local\programs\python\python36-32\lib\site-packages (from djangorestframework) (3.2.13)
Requirement already satisfied: asgiref<4,>=3.3.2 in c:\users\admin\appdata\local\programs\python\python36-32\lib\site-packages (from django>=3.0->djangorestframework) (3.4.1)
Requirement already satisfied: sqlparse>=0.2.2 in c:\users\admin\appdata\local\programs\python\python36-32\lib\site-packages (from django>=3.0->djangorestframework) (0.4.2)
Requirement already satisfied: typing-extensions in c:\users\admin\appdata\local\programs\python\python36-32\lib\site-packages (from asgiref<4,>=3.3.2->django>=3.0->djangorestframework) (4.1.1)
Installing collected packages: djangorestframework
Successfully installed djangorestframework-3.14.0





How to use (Installing) django rest framework in our Django Project: 👍

In our project - in default app's settings.py file, in 
💡
INSTALLED_APPS = [
'rest_framework',
]

# https://www.django-rest-framework.org/


# that's it, once we added rest_framework in installed_apps, now we can using rest framework can create web api
👍
# Web API responses (data sending) to broswer or mobile are formatted in JSON - (JavaScript Object Notation) or XML Format.

# as world-wide json mostly used to send data through web api to browser or android mobile or apple mobile


