
# Django Templates: ✅
# Web Application Result or Output should be in HTML Format,  
# and it should be created in a templates 
# so we need to render (provide) template (design) to show our output in a good design 🙌

# Step 1) Create Folder as templates in our project  
# Step 2) In settings.py file - search templates and to DIRS key give value in the list base directory of templates folder then only server will search templates folder and in that folder .html files should be available 👍

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],   
        'APP_DIRS': True,

# below line is the value of DIRS Key, we just need to add in DIRS [] sqaure bracket below path, it means we are configuring templates directory where our all .html (design) files are available. 👍

'DIRS': ["templates"],
# Just add templates (folder name where we keep all design files) in square brackets in double quote

or

import os    ✅
 
os.path.join(BASE_DIR, "templates")

# In settings.py file import os then only os.path.join() will run

# once set the base dir then create any .html file and change views.py file
# as before we give static data when default page will run but now we are opening .html file.

# Therefore now we need to use below render() function to access .html file

return render(request,'index.html')

# Write in views.py in index() function as default index() function will run



















