from django.shortcuts import render 
from django.http import HttpResponse


# Create your views here.
# def home(request):

def home(request):
    return render(request, 'index.html')




# def index(request):
#        return HttpResponse('''<h1>Travling with vikas</h1> <a href="https://youtu.be/Vq0j9_Jf3BI?si=tsxZhzt8dRLMpLu_">traval with 🫡</a>  <br><br><a href='/'>back</a>''')

# def home(request):
#       return HttpResponse('''this is my first time try to code in english' <a href='/'>back</a>''')

# def contact(request):       return HttpResponse(' call the police with vikas ')