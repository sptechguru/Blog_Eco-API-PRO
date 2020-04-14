
from rest_framework import serializers
from myapp .models import MyContact ,MyProdcut ,MyOrders ,MyOrderUpdate


class MyProdcutSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProdcut
        fields = "__all__"

class MyOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyOrders
        fields = "__all__"


class MyOrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyOrderUpdate
        fields = "__all__"      


class MyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyContact
        fields = "__all__"
