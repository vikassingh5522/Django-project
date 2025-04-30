# To open admin login, we need to create superuser with username and password,
# before that, We need to run command as:👍
py manage.py makemigrations 

# When we run makemigrations command, below output will display on terminal as:

PS C:\Users\admin\Desktop\DJango Programs\Testing\Project_ZEAL> py manage.py makemigrations
System check identified some issues:

WARNINGS:
←[33;1m?: (urls.W005) URL namespace 'admin' isn't unique. You may not be able to reverse all URLs in this namespace←[0m
No changes detected


# using makemigrations - Database schema (structure) will create
# makemigrations create some files using we can create tables
# Sequel information which we use to create table
# makemigrations convert python class into sequel friendly format and then that format run a sequel in order to populate the database.

# Django creates a file with any new changes and stores the file in the /migrations/ folder.

# Next time you run py manage.py migrate Django will create and execute an SQL statement, based on the content of the new file in the migrations folder.

# and then again run command as: 👍

py manage.py migrate

# When you run migrate command, below execution will perform and output will display as:

PS C:\Users\admin\Desktop\DJango Programs\Testing\Project_ZEAL> py manage.py migrate
System check identified some issues:

WARNINGS:
←[33;1m?: (urls.W005) URL namespace 'admin' isn't unique. You may not be able to reverse all URLs in this namespace←[0m
←[36;1mOperations to perform:←[0m
←[1m  Apply all migrations: ←[0madmin, auth, contenttypes, sessions
←[36;1mRunning migrations:←[0m
  Applying contenttypes.0001_initial...←[32;1m OK←[0m
  Applying auth.0001_initial...←[32;1m OK←[0m
  Applying admin.0001_initial...←[32;1m OK←[0m
  Applying admin.0002_logentry_remove_auto_add...←[32;1m OK←[0m
  Applying admin.0003_logentry_add_action_flag_choices...←[32;1m OK←[0m
  Applying contenttypes.0002_remove_content_type_name...←[32;1m OK←[0m
  Applying auth.0002_alter_permission_name_max_length...←[32;1m OK←[0m
  Applying auth.0003_alter_user_email_max_length...←[32;1m OK←[0m
  Applying auth.0004_alter_user_username_opts...←[32;1m OK←[0m
  Applying auth.0005_alter_user_last_login_null...←[32;1m OK←[0m
  Applying auth.0006_require_contenttypes_0002...←[32;1m OK←[0m
  Applying auth.0007_alter_validators_add_error_messages...←[32;1m OK←[0m
  Applying auth.0008_alter_user_username_max_length...←[32;1m OK←[0m
  Applying auth.0009_alter_user_last_name_max_length...←[32;1m OK←[0m
  Applying auth.0010_alter_group_name_max_length...←[32;1m OK←[0m
  Applying auth.0011_update_proxy_permissions...←[32;1m OK←[0m
  Applying auth.0012_alter_user_first_name_max_length...←[32;1m OK←[0m
  Applying sessions.0001_initial...←[32;1m OK←[0m


# Using migrate command - create tables as per models.py forms  👍

# and then type in terminal:
py manage.py createsuperuser  👍

Username (leave blank to use 'admin'):   👍

# Give name as superuser as we are creating super user because in super user login we can create admin,
# using we can login and see information which we send to database

Email address: 👍
# Email address is optional

Password: 👍
# When you enter password it will not show on screen but it accepting your password, which you are typing

Password (again):

←[31;1mThe password is too similar to the username.
←[0mBypass password validation and create user anyway? [y/N]: y

# Above message is just about password is simillar to username, are you sure want to continue, we can press y 

superuser created successfully.

# Once we got this message, now you can check http://127.0.0.1:8000/admin   -   You will get superadmin login page


# if you want to change password of super user:
py manage.py changepassword <username> 😰🤷‍♂️


# If you want to change after login dashboard Django administration text,
# then below three lines you need to add in your 

  default app's urls.py file

from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Elite Softwares Admin"
admin.site.site_title = "Elite Softwares Admin Portal"
admin.site.index_title = "Welcome to Elite Softwares Portal"


# above to urlpatterns as:


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
        
]  













