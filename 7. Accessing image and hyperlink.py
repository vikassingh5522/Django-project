Accessing images on Website using Django framework

# We need to save all images or pdf all, static files in static folder only, as we can not keep images in templates folder because templates keyword not recognize by django it will show this error:
 
'templates' is not a registered tag library. Must be one of:
admin_list
admin_modify
admin_urls
cache
i18n
l10n
log
static
tz
 
# We need to add above to <!DOCTYPE html> tag in .html page

{% load static %} ✅  

# {% %} means passing template tags through Django into html file 👍

# where static is the system predefined keyword so in static folder we need to save our static data as images, .pdf, .doc, etc.

# and we need to load in that .html file before giving path of that image
# and using <img src=""/> tag we can access image as:
<img src="{% static "images/dypmca.jpg" %}" />✅

<img src="images/abc.jpg"/>

How to use Hyperlink (Menu) using DJango:-
# syntax : <a href="{% url 'name of that page which we give in urls.py of Home app' %}">👍

<a href="{% url "contactus" %}">Contact Us</a> ✅

<a href="index.html"> Home </a>