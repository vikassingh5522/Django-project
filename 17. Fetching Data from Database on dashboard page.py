# Once admin login done, we need to show enquiry form details to admin
# from database.

# add in website -> urls.py file - 
from website.models import enquiry_table


path('dashboard', views.dashboard, name = 'dashboard'),
# Now We need to create function for Dashboard on this page we want to show data

# import that model which we want to create function in views.py

# in views.py -> 
def dashboard(request):
    info = table_name.objects.all()
    # contact is table name which we create in models.py
    data = {'information':info}
    return render(request, 'dashboard/dashboard.html',data)

# We need to send queryset to template from table
# in html form action="dashboard" should be mention, 
# dashboard page or where we want to show data
# using dictionary queryset means where data is available sent to template and using for loop using template tags we can display data.

# modelname.objects.all() function use to fetch the data from that model
# it means all information which is available at contact model it will store in info named variable




