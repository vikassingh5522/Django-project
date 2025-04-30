CRUD Operations in Django Admin Design - Edit and Update Records

        
Now on click to Edit button, that record information we can change,
so we need to fetch that particular record and then we need to update that information which we want to change. 

For Edit and Update operations we required a new function and for new function we required a new url in urls.py file,

so add new url and new function for edit and update operation.

     <td>
        <a href="{% url 'edit_record' info.id %}"> <button type="button" class="btn btn-info"> Edit </button>
        </a>
    </td>




path('edit/<int:id>/', views.edit_record, name ='edit_record'),

# <> Django dynamic url - using this tag we can have data dynamic from another page, 
# on click to Edit button, that selected record id send by tables.html page using <form> tag
# and that selected id catch in path() of urls.py
# and then using function() we need to fetch data of selected records on seperate new .html page

# So create new .html page - editrecords.html, and in this page we can fetch selected records data and then on that page we can perform update operation


def edit_record(request, id):
    info = table_name.objects.filter(pk=id)
    # Use filter() for fetching number of records same time, get() fetch only one record but we want same time all records which is available in table, therefore use filter(pk=id)

    data = {'information':info}
    return render(request, 'dashboard/editrecord.html', data)

# we need to render that page where we want to show data and from that .html page, we can change information and then update

# Here we create new page as editrecord.html, and where data we want at that location just we take one form.

# Remove table card div and add below form where we want information which we want to edit.


Now we can fetch data in below form:

{% for info in information %}

# We need to start for loop for get the data which is available in information key
# and close for loop also end of the section

<section class="ftco-section ftco-no-pt ftco-no-pb contact-section">
                <div class="container">
                  <div class="row d-flex align-items-stretch no-gutters">
                    <div class="col-md-6 p-4 p-md-5 order-md-last bg-light">
                      <form action="{% url 'update_record'  info.id %}" method="POST" name="Edit_Form">
                        <input type="hidden" name ="id" id="id" value="{{info.id}}">

                        # above <input> tag will fetch that selected record on which we click

                        {% csrf_token %}
                <!-- Cross-Site Request Forgery (CSRF) is an attack that forces authenticated users to submit a request to a Web application against which they are currently authenticated.
                CSRF Token used to prevent unathorized person could not submit form from your website-->
                        <div class="form-group">
                          <input type="text" class="form-control" name="name"  value="{{info.name}}" required>
                        </div>
                        <div class="form-group">
                          <input type="email" class="form-control"  name="email" value="{{info.email}}" >
                        </div>
                        <div class="form-group">
                          <input type="text" class="form-control"  name="phone" value="{{info.phone}}" >
                        </div>
                        <div class="form-group">
                          <input type="text" name="address"  cols="30" rows="7" class="form-control"  value="{{info.message}}" >
                        #   <textarea> change to <input> tag then only data will display
                        </div>
                        <div class="form-group">
                          <input type="submit" value="Update" class="btn btn-primary py-3 px-5" name="submit">
                        </div>
                      </form>
                    </div>
                  
                  </div>

                </div>
              </section>

{% endfor %}


Now once data fetching on form, we need to update data as:

where we fetch data on same form in front of action="" you need to send changed data to function() for execution means update query run

# for that we need to create new path() and function() for update_record

# When Update button clicked, below action page will call and dynamic url id will send for changes

<form action="{% url 'update_record'  info.id %}" method="POST" name="Edit_Form">

# In urls.py file, need to add update path()

path('update/<int:id>/', views.update_record, name ='update_record'),


# In views.py file, need to add update()

def update_record(request, id):
    info = enquiry_table.objects.get(pk=id)
    
    info.name = request.POST.get('name')
    info.email = request.POST.get('email')
    info.phone = request.POST.get('phone')
    info.message = request.POST.get('message')
    info.save()
    
  # info.name, info.email because that particular records we want to update not all column data.

    return HttpResponseRedirect('/info/')

# '/info/' path name of on which page all records showing






























