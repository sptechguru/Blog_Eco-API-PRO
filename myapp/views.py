from django.shortcuts import render,HttpResponse,redirect
from rest_framework import generics
from myapp.models import MyContact ,MyProdcut ,MyOrders ,MyOrderUpdate
from .serializers import MyContactSerializer ,MyProdcutSerializer ,MyOrdersSerializer ,MyOrderUpdateSerializer


# Create your views here.

def index(request):
    return render(request,'myapp/index.html')

class MyContactAPIView(generics.ListCreateAPIView):
	queryset = MyContact.objects.all()
	serializer_class = MyContactSerializer


class MyProdcutAPIView(generics.ListCreateAPIView):
	queryset = MyProdcut.objects.all()
	serializer_class = MyProdcutSerializer	



class MyOrdersAPIView(generics.ListCreateAPIView):
	queryset = MyOrders.objects.all()
	serializer_class = MyOrdersSerializer


class MyOrderUpdateAPIView(generics.ListCreateAPIView):
	queryset = MyOrderUpdate.objects.all()
	serializer_class = MyOrderUpdateSerializer