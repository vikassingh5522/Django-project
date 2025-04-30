# Accessing Static Files through Web Server using Django Framework: ✅

# Create a Static folder inside the Project in this example Project_Name 👍

# Note: In the project default app settings.py file - You need to add base directory to open static folder which is available in our project 👍

# https://docs.djangoproject.com/en/3.2/howto/static-files/  🫡

# Above link for how to Configure static files

# You need to add below list in settings.py file which is available in default app 👍

STATICFILES_DIRS = [
                    BASE_DIR / "static",
                    '/var/www/static/',
                    ]

# OR                                        👇

STATICFILES_DIRS = [
                   os.path.join(BASE_DIR,  "static")
                    ]

# Note: if you uses second link, You need to import os module for second option in settings.py file

# Note : Add above staticfiles dirs varialable in settings.py file of project then only static files we can access through server 👍

