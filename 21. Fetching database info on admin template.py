# Now in admin dashboard, we need to fetch database table information which inserted through enquiry form

In tables.html page where table format form is available where we suppose to show information to admin

In that .html page, we need to use for loop in django tags and fetch the data from enquiry_table where we store our data as:

                <div class="card">
                <div class="card-body">
                  <h5 class="card-title">Basic Datatable</h5>
                  <div class="table-responsive">
                <table
                      id="zero_config"
                      class="table table-striped table-bordered">
                      <thead>
                        <tr>
                          
                          <th>Sr. No.</th>
                          <th>Name</th>
                          <th>E-Mail Id.</th>
                          <th>Mobile No.</th>
                          <th>Message</th>
                          
                        </tr>
                      </thead>
                      <tbody>
                        
                    # delete all dummy data below of <tbody> tag till </tbody> and use in django code to access data from table of actual information which is stored in table.

# as here in tables.html page we want to fetch data from database, therefore in that page function which we write in views.py we need to collect data from table and then send on .html page through dictionary as:

# def enquiry_info(request):
# info = enquiry_table.objects.all()
# # enquiry_table is table name which we create in models.py

# data = {'information':info}
# return render(request, 'dashboard/tables.html', data)    

# Basically on which page we want to display data from database, on that function() we need to collect data and send through dictionary.

# and using for loop catch that data on .html page

                        {% for x in information %}
                            <tr>
                            <th scope="row">{{ forloop.counter }}</th>
                            <td>{{ x.name }} </td>
                            <td>{{ x.email }}</td>
                            <td>{{ x.phone }}</td>
                            <td>{{ x.address }}</td>
                            </tr>
                        {%  endfor %}
                      </tbody>
                </table>


        # To execute logout function(), link logout() name using django tags

        {% url "logout" %}

        # it will call logout path and session will be logout