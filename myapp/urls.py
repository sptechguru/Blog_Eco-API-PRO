from django.contrib import admin
from django.urls import path ,include
from myapp import views

urlpatterns = [

path('',views.index,name='index'),

path(r'Prodcut/', views.MyProdcutAPIView.as_view(),name='MyProdcut'),
path(r'contact/', views.MyContactAPIView.as_view(), name='MyContact'),
path(r'orders/', views.MyOrdersAPIView.as_view(), name='MyOrders'),
path(r'update/', views.MyOrderUpdateAPIView.as_view(), name='MyOrderUpdate')



]