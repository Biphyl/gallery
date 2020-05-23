from django.urls import path
from . import views

urlpatterns=[
    path('',views.photo_of_day,name= 'Welcome'),
    path('today/',views.photo_of_day,name='photoToday'),
    path(r'archives/(\d{4}-\d{2}-\d{2})/',views.past_days_photos,name= 'pastPhotos')
]