from django.urls import path
from .views import register,signin,signout,home

#this are the url patterns that matches to view function 
urlpatterns = [
    path('register',register,name='register'),
    path('',home,name='home'),
    path('signin',signin,name='signin'),
    path('signout',signout,name='signout')
]