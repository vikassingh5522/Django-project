Browsable APIView : 

# Showing data thorugh web api but in browsable view for that we need to do some changes in views.py as well urls.py

# in views.py we need to add few modules as:

from rest_framework.response import Response
from rest_framework.views import APIView

# Now in views.py instead of function we need to create class and in that class, create view as get() and post()

class student_data(APIView):
    def get(self, request, format=None):
        data = enquiry_table.objects.all()
        serializer = enquiry_tableSerializer(data, many=True)
        return Response(serializer.data)

# path('student_data', views.student_data.as_view(), name ='student_data'),
# for browsable apiview data you want to fetch, then in urls.py above path you need to add
# views.student_data.as_view() - calling class as a function

