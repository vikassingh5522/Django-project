# Django Matrix Admin Template we are going to use to display dashboard to admin after successfull login

# Django Admin LTE is also very popular world-wide admin template

# Graphical Presentation - view to admin where Application Development all pages modules will create and show to admin only(login required).

https://matrixadmin.wrappixel.com/

# From above link you can easily downlpad matrix admin from internet
# On google search : django matrix admin, you will get above link

step 1) Download template
step 2) create one folder in templates folder as dashboard
step 3) keep all .html designs in dashboard folder (basically admin related designs files we are keeping in seperate folder that is dashboard)
step 4) assets, dist, src these all static folder copy and paste in static folder (as all static files we keep in static folder in django), again to keep files of front end and backend create one folder in static folder also as dashboard.

# Now you can run and check project, it will show matrix admin page without css, js, images

# For accessing css, js and images, Now you need to use django tags to access .css, .js, etc all properties of templates from static folder

Open index.html file from dashboard folder and change .css, .js, .jpg, etc path to django template path as 
{% static "location of css or js or images" %}

Use find and replace method 
use propoer django template tags then only design css, js and images will display on page

Now which page you want keep those pages link in href="" remaining all href="#" link should be #, so page not found error should be come

and those pages you want, again in that pages also you need to change .css, .js and .png images path with django tags

Note: Those pages now if you don't want just comment those menus <li> </li> and keep working menus only when you required other menus then again you can un-comment and use












