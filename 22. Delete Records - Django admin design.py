CRUD Operations in Django Admin Design - Delete Records with Confirmation Message

# In Django admin design - where we fetching data from database, on same table now will see
# records Edit, Update and Delete Operations

Now we have table format information from database, in same .html page in the table format, we need to add 
Edit and Delete link or Button for Operations.
(In this example, table information we fetch in tables.html page)

        <thead>
        <tr>
            <th>Sr. No.</th>
            <th>Name</th>
            <th>E-Mail Id.</th>
            <th>Mobile No.</th>
            <th>Message</th>
            <th>Edit</th>
            <th>Delete</th>
            
        </tr>
        </thead>
        <tbody>



        {% for info in information %}
            <tr>
            <th scope="row">{{ forloop.counter }}</th>
            <td>{{ info.name }} </td>
            <td>{{ info.email }}</td>
            <td>{{ info.phone }}</td>
            <td>{{ info.address }}</td>
            <td> Edit </td>
            <td><button type="button" class="btn btn-danger">Delete</button></td>

            # if you want Button instead of normal text, this bootstrap button class you can use
            # <button type="button" class="btn btn-danger">Delete</button>

            </tr>
        {%  endfor %}


Now on click to delete button, that record should be deleted, 
For delete operation we required a new function and for new function we required a new url in urls.py file,

so add new url and new function for delete operation.

before that you need to take one form for delete button click, where actual record we are fetching for delete that particular record,

    <td> 
    <form action="{% url 'delete_record' info.id %}" method="POST">

    # info.id - is a dynamic url, we are sending button click id record to delete_record page and using delete_record() calling, operation will execute.

    {% csrf_token %}

    <input type="submit" value="Delete" class="btn btn-danger" >

    </form> 
    </td>


path('delete/<int:id>/', views.delete_record, name ='delete_record'),

# <> Django dynamic url - using this tag we can have data dynamic from another page, 
# on click to delete button, that selected record id send by tables.html page using <form> tag
# and that selected id catch in path() of urls.py
# and then using function() we can perform delete operation


def delete_record(request, id):
    if request.method=='POST':
        data = table_name.objects.get(pk=id)
        data.delete()
    return HttpResponseRedirect('/info/')

# HttpResponseRedirect('/info/') - after delete again user should be on same page - and info/ is tables.html path name which we give in urls.py file

# In views.py we need to import module as:
from django.http import HttpResponseRedirect


# Now to show Confirmation message on Deleting Records, we need to add in <form> tag onsubmit query as:

<td>  <form action="{% url 'delete_record' info.id %}" method="POST" onsubmit="return confirm('Are you sure, you want to delete record..')">

