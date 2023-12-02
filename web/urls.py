from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('Update/',views.Updates,name='Update'),
    path('blog-details/',views.blogdetails1,name='blog-details-1'),
    path('Profile/',views.Profile,name='Profile'),
    path('Business-Sector/',views.Business_Sector,name='Business-Sector'),
    path('Award/',views.Awards,name='Award'),
    path('Contact/',views.contact,name='Contact'),
    path('Gallery/',views.Gallery,name='Gallery'),

      
]