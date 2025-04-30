from django.contrib import admin
from django.urls import path
from application import views
# from index import views


urlpatterns = [
    #  path('admin/', admin.site.urls),
    #  path('home',views.home,name='Home'),
    #  path('index',views.index,name='index'),
    #  path('',views.contact,name='cont'),
    
      path('', views.home, name='Home'),
]