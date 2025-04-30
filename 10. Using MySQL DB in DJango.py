# As Default DJango framework database is SQLite but if you want to change database to MySQL then we need to perform few steps as:

# step 1: Open MySQL Dashboard and create one database for your project.

# step 2: as default DB is SQLite so we need to change from settings.py file in DATABASE Dictionary as:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Change to:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Database_Name',
        'USER':'root',
        'PASSWORD':'',
        'HOST':'127.0.0.1',
        # Open MySQL dashboard and check on which ip (or localhost) your mysql is running
        'PORT':'3306', 
        # 3306 is the default port number
    }
}

# After this when you run project, you will get error as:
django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module.
Did you install mysqlclient?

# Means now you have to install mysqlclient library in your python (system)

# step 3: Open Command Prompt and install mysqlclient as:

pip install mysqlclient

# during installation if you get red color error means mysqlclient exucutable file is not available in your system so need to find .whl (wheel) file exucutable file for mysqlclient.

https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient

Open this link and download as per your python version .whl file and after download .whl file,
keep that file where python is installed means c:\users\admin (check you installed python)

# as in my system 3.6.7 version is installed so I downloaded:
mysqlclient-1.4.6-cp36-cp36m-win32.whl  this file.

# step 4: Now open command prompt and type :
c:\Users\admin: pip install mysqlclient-1.4.6-cp36-cp36m-win32.whl

# after file name just enter, it will now install mysqlclient above version file in your system.

# and you will get Successful message as mysqlclient is installed..

Now you can run django project and check it will show ip address where django projects run.


step 5: After this process, we need to run py manage.py makemigrations and py manage.py   migrate command to show default tables in Database which we create in MySQL.

# Now you can see MySQL dashboard, you will get all 10 default tables of django project and which we create table in django in models.py, that also we can see in MySQL dashboard and operate also.

This way to change default SQLite DB to MySQL DB.



