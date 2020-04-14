

from django.shortcuts import render,HttpResponse,redirect
from rest_framework import generics
from .models import MYPost, MyContact 
from .serializers import MYPostSerializer, MyContactSerializer 


# def index(request):
#     return render(request,'blog_api/index.html')

class MypostAPIView(generics.ListCreateAPIView):
    queryset = MYPost.objects.all()
    serializer_class = MYPostSerializer

class MycontactAPIView(generics.ListCreateAPIView):
    queryset = MyContact.objects.all()
    serializer_class = MyContactSerializer






    # from rest_framework import viewsets
# from . import models
# from . import serializers

# class MyPostViewset(viewsets.ModelViewSet):
#     queryset = models.MyPost.objects.all()
#     serializer_class = serializers.MYPostSerializer

# class MyContactViewset(viewset.ModelViewSet):
#     queryset = models.MyContact.objects.all()
#     serializer_class = serializers.MyContactSerializer



# class ActivityStatusAPIView(generics.ListCreateAPIView):
#     queryset = ActivityStatus.objects.all()
#     serializer_class = ActivitySerializer

# class ContactAPIView(generics.ListCreateAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer

# class ContactStatusAPIView(generics.ListCreateAPIView):
#     queryset = ContactStatus.objects.all()
#     serializer_class = ContactSerializer

# class ContactSourceAPIView(generics.ListCreateAPIView):
#     queryset = ContactSource.objects.all()
#     serializer_class = ContactSourceSerializer

