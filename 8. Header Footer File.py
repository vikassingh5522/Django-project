
# Create separate header.html file and write a code of banner and menu
# once created header.html header file then in other .html files using

{% include 'header.html' %}  ✅

# using this syntax you can add header file in other .html pages

# This way every time no need to changes in every pages.

# Simillarly create footer.html file also.✔️

extends

# The extends tag allows you to add a parent template for the current template.

# This means that you can have one master page that acts like a parent for all other pages:

# Create Master👍 base.html file in that write this below code. 


{% include "header.html" %} ✔️

{% block content %}   ✔️


{% endblock %} ✔️ 

{% include "footer.html" %}✅


# On the TOP of index.html or any other page now we need to call 
{% extends 'base.html' %}✅

{% block content %}✅
{% load static %}✅ 
<html>
<head>
	<title> DJango - Project 3 - Admin User </title>
    ....
    ....
</body>
</html>	
{% endblock %}✅


