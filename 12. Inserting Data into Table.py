# Once check on which page our enquiry form is available

# In this example, we have form on contactus page

# So in contactus() which is available in views.py file, in this function we need to writedown insert query as:

# as we are using in this file enquiry_table therefore we need to import table name as:✅👇

from website.models import enquiry_table 👍

def contactus(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('phone')
        d = request.POST.get('message')
        enquiry = enquiry_table(name = a, email = b, phone = c, message = d)
        enquiry.save()

        messages.success(request, 'Enquiry Form Submitted Successfully...') ✅
        
    return render(request, 'contact.html')

# Now you can check superadmin login, Enquiry Form Sent Successfully... 😀

# After submit form there is NO confirmation to user as user expect some messages should display as Enquiry Sent Successully or Not

For showing messages to User we can use these default django messages as:

Before using any function of messages, we need to first import one file that is:

from django.contrib import messages

# Above module we need to add in views.py file

messages.info(request, 'Three credits remain in your account.')
messages.success(request, 'Profile details updated.')
messages.warning(request, 'Your account expires in three days.')
messages.error(request, 'Document deleted.')

# Use any message you want as per your message type, use any function after data save in views.py file

# and where enquiry form is available, in that page means in contactus.html page, use below code as:

           <div class="row">
              {% for x in messages %}
                  <center>
                  <h5> 
                  
                    <div class="alert alert-warning alert-dismissible fade show" role="alert">
                       <strong style="color:green;">{{x}}</strong>
                      <button type="button" class="close" data-bs-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                      </button>
                    </div>
                                      
                  </h5>
                  </center>
              {% endfor %}
          </div>  
