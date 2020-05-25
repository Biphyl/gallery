from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns=[
    # path('',views.photo_today,name = 'photoToday'),
    path('',views.index,name='index'),
    path(r'archives/(\d{4}-\d{2}-\d{2})/', views.past_days_photos, name = 'pastPhotos'),    
    path(r'search/', views.search_results, name='search_results'),
    path(r'category/(\d+)',views.category,name ='category')
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)