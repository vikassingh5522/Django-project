Serializers and Serialization in Django REST Framework : 💡😀

# Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types for easily readable by Front-End. 

# Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.

# to complete this process we need to create serializers class where we serialize (convert) data into python datatype and then only complex data means queryset objects (SQLite DB records) convert into native Python datatypes and then easily using python json package using dumps() and loads() method easily data can convert into string and vice-versa 

# Note: What is QuerySet: A QuerySet represents a collection of database query results, typically matching certain criteria. It acts as a high-level, Pythonic representation of the SQL queries that would be executed to retrieve data from the database. Instead of writing raw SQL queries, developers can use QuerySets to perform various database operations such as filtering, sorting, aggregating, and more.


How to create Serializer Class: 💡😀

step 1) create a seperate serializers.py file in your app where you can write all serializers in this new file.

In that serializers.py file: 🗃️ create a file 

from rest_framework import serializers  ✔️

# as serializers module is in rest_framework package therefore we need to import ✅

class enquiry_tableSerializer(serializers.Serializer):
    # Rememer serializers.Serializer - S is capital of Serializer
    name = serializers.CharField(max_length=100)
    mobile = serializers.IntegerField(max_length=10)
    

    fields= '__all__'
    # it will serialize all fields which are available in table_name which we create from models.py

# Here in this serializers.py file work is done, now using views.py file using function we can access this class and work on serialization concept


Step 2) Now the process of Serialization :  📝


# Means converting queryset data converting into native python datatype and then using json send data on front-end 

# Serialization process done in views.py file under new method for rest api, create new function and write serialization process.

1) Creating Query Set Object 
    data = enquiry_table.objects.all()
    # enquiry_table is table name, using above sentence for all records we create one object that is data


 2) Now Converting model instance to Serializing Object 
    serializer = enquiry_tableSerializer(data, many=True)
    # many=True argument we need to pass as in table we have multiple records therefore we have to mention
    # and here data object now we are converting into serialization
    # and after that using serializer object we can perform further steps means sending data to json and json will send data to front-end

serializer.data - dafault variable

# and using serializer.data default variable we can access serialized data, which is now available in serializer object

JSONRenderer :

Using this Module and Method we can render (provide) serialized data into JSON which is understandable or readable by any Front-End.


# so we need to import JSONRenderer module and method to convert serialized data into JSON

from rest_framework.renderers import JSONRenderer

json_data = JSONRenderer().render(serializer.data)

# Above sentence is Rendering Serialized data into json data

and then using return branching statement, we can return json_data to Front-End using HttpResponse()


So need to create path() in urls.py file and from where url hit and above student_data() function will execute and other web application or any device can access this data.

In urls.py file :

from django.contrib import admin
from django.urls import path
from website import views

urlpatterns = [
    
    path('student_data', views.student_data, name ='student_data'),

]

# So now student_data will be Resource of API or End-Point, using data will be fetch.

and in views.py file, REST Web API function looks like:

from .models import enquiry_table
from .serializers import enquiry_tableSerializer
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def student_data(request):
    data = enquiry_table.objects.all()
    # Creating Model instance
    
    serializer = enquiry_tableSerializer(data, many=True)
    # Converting model instance to serialized data

    # json_data = JSONRenderer().render(serializer.data)
        # Converting serialized data into JSON String

    # return HttpResponse(json_data, content_type='application/json')
        # Returning json string through HttpResponse()
        # and we need to specify content type here.

    return JsonResponse(serializer.data, safe=False)
    # In order to allow non-dictionary objects to be serialized set the safe parameter to False.
    
    # Default first parameter as serializer.data accepts only dictionary value therefore non dictionary value if we are passing then safe=False we need to set else above error show

    # In JsonResponse() no need to write content_type as default type is application/json in JsonResponse()

# Instead of JSONRenderer() and HttpResponse() we can use JsonResponse() to get the json data on browser.













































