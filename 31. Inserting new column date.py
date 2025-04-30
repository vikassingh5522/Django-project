
# After table create in models.py, as for getting reports from-date to to-date, we required date column compulsory, so will see how we can take current date while submitting form from front end.

# As we required current date, so we need to take date column in our table using models.py

In models.py file we need to add new coulmn as:

date_field = models.DateField(default=date.today)

and import date module in same models.py file as 

from datetime import date

# As for any change in models.py file we have to run 2 commands, those are makemigrations and migrate command.

So run in terminal py manage.py makemigrations 

After that py manage.py migrate

# and Now you can check in mysql database date column is added with today's default date


# Now we need to fetch date column where table information we are fetching for client as,

                          <th>Enquiry Date</th>
                      #     <th>Edit</th>
                      #     <th>Delete</th>
                      #   </tr>
                      # </thead>
                      # <tbody>
                       

                      #   {% for x in information %}
                      #   <tr>
                      #   <th scope="row"  style="text-align:center;">{{ forloop.counter }}</th>
                      #   <td>{{ x.name }} </td>
                      #   <td>{{ x.email }}</td>
                      #   <td>{{ x.phone }}</td>
                      #   <td>{{ x.message }}</td>
        ``                <td>{{ x.date_field }}</td>

# default MySQL date format is yyyy-mm-dd, if you want to change date fotmat for display purpose then:

 <td>{{ x.date_field|date:"d-M-Y" }}</td>

#  Now you can see in table, date format will show dd-mm-yyyy,

# after that click to edit button and new editpage will open,
# here also we need to add new date field and fetch date in format of yyyy-mm-dd format therefore we fetch date in yyyy-mm-dd format, because default MySQL data format.

                        <div class="form-group">
                          <input type="text" name="date"  cols="30" rows="7" class="form-control"  value="{{info.date_field|date:"Y-m-d"}}" >
                        </div>


# and for this updating data we are calling update_record() to update the data.
# so fetch updated date in this function and save records as :

# def update_record(request, id):
#     info = driver_table.objects.get(pk=id)
    
#     info.name = request.POST.get('name')
#     info.email = request.POST.get('email')
#     info.phone = request.POST.get('phone')
#     info.message = request.POST.get('message')
      info.date_field = request.POST.get('date')
      # info.save()
    
    # return HttpResponseRedirect('/driver-info/')






