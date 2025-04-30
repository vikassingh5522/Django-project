DJango Reports:👍

# As in Every Project Reports are very important to show filtered data to client on selection from date and to date fetching records.

# We need to take one new page for Reports where we can show reports which clients wants.

# Add a new .html page in dashboard folder and then one new path in urls.py and new function in views.py.

# Now in reports.html page on selection from date and to date we need to show the data, for we need to add date picker fields just above to <table> tag using <form> tag.

            <div class="card">
                <div class="card-body">
                  <h5 class="card-title">Reports Generation:</h5>
                  <div class="table-responsive">
                   
                   
                    <hr>
                      <form  action="{% url 'reports' %}" method="POST">
                          {% csrf_token %}
                           From: <input type="date" name="fromdate">
                           To: <input type="date" name="todate">
                           <input type="submit" class="btn btn-success" value="Search">
                      </form>
                    <hr>
                   
                    <table
                      id="zero_config"
                      class="table table-striped table-bordered"
                    >

                      <thead>
                        <tr>
                          <th>Sr. No.</th>
                          <th>Name</th>
                          <th>E-mail Id</th>
                          <th>Mobile Number</th>
                          <th>Message</th>
                          <th>Date</th>
                          <th>Edit</th>
                          <th>Delete</th>
                        </tr>
                      </thead>

# After </table> tag closing, close form tag

# Here we take one form for selection from date and to date input type is date as we want date selction.

Now in tha reports function, we need to from date and to date from user and accordingly fetch data from table as :

from datetime import datetime

def reports(request):

    data = None
    # local variable 'data' referenced before assignment, this error will show if we did not give None value to data variable before function start.

    if request.method=='POST':

        # from date and to date store into variable from form field data.
        from_date = request.POST.get('fromdate')
        to_date = request.POST.get('todate')
     
        # Convert the date strings to datetime objects
        
        from_date = datetime.strptime(from_date, '%Y-%m-%d').date()
        to_date = datetime.strptime(to_date, '%Y-%m-%d').date()

        # as we are using strptime() function from datetime module so we need to import datetime module in views.py file as:

        
        # The strptime() method creates a datetime object from the given string.

        # Fetch the data from the table based on the date range
        searchresult = driver_table.objects.filter(date_field__range=[from_date, to_date])

        data = {"information":searchresult}
        
    return render(request, 'dashboard/reports.html', data)





