from django.urls import path
from . import views

urlpatterns=[
    path('',views.welcome,name= 'Welcome'),
    path('today/',views.photo_of_day,name='photoToday')
]