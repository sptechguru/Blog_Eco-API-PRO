from django.contrib import admin
from django.urls import path ,include
from blog_api import views

urlpatterns = [

# path('',views.index,name='index'),

path(r'mypost/', views.MypostAPIView.as_view(),name='mypost'),
path(r'mycontact/', views.MycontactAPIView.as_view(), name='mycontact')


]