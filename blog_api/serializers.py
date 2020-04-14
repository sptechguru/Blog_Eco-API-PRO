
from rest_framework import serializers
from blog_api .models import MyContact ,MYPost


class MYPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = MYPost
        fields = "__all__"

class MyContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyContact
        fields = "__all__"
