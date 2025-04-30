# DJango Models:

# A model is the single, definitive (final) source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.

# The basics:

#     Each model is a Python class that subclasses django.db.models.Model.
#     Each attribute of the model represents a database field.
#     With all of this, Django gives you an automatically-generated  database-access API;

# A Django model is a table in your database.
# SQLite Database is a default Database of Django
# When we created the Django project, we got an empty SQLite database. It was created in the Project root folder.

# Create Table (Model)
# To create a new table, we must create a new model.

# In the /application/ folder, open the models.py file. It is almost empty by default, with only an import statement and a comment

# application/models.py:

from django.db import models

# Create your models here.✔️


class enquiry_table(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.name



# Fields DataType : https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types


We need to register models (table which we create) in application (our app name) -> admin.py file -> import file as


from django.contrib import admin
from website.models import enquiry_table
# Register your models here.

admin.site.register(enquiry_table)  🫡

# - enquiry_table is table name which we create in models.py file


# once in models.py class is created means table we are creating as per form fields, then we need to run makemigrations and migrate command to read models.py file. 

py manage.py makemigrations 🆗 1 call

System check identified some issues:
WARNINGS:
←[33;1m?: (urls.W005) URL namespace 'admin' isn't unique. You may not be able to reverse all URLs in this namespace←[0m
←[36;1mMigrations for 'Home':←[0m
  ←[1mHome\migrations\0001_initial.py←[0m
    - Create model contact

# Once you run command, above message will display in terminal.

# Then type another command
py manage.py migrate 🆗 2 call

System check identified some issues:
WARNINGS:
←[33;1m?: (urls.W005) URL namespace 'admin' isn't unique. You may not be able to reverse all URLs in this namespace←[0m
←[36;1mOperations to perform:←[0m
←[1m  Apply all migrations: ←[0mHome, admin, auth, contenttypes, sessions
←[36;1mRunning migrations:←[0m
  Applying Home.0001_initial...←[32;1m OK←[0m

# Above message will display on terminal means contact named table is created in database.


# DJango will create a table of name contact now in your default database


