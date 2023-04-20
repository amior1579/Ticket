from .models import *
from rest_framework import serializers



class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username','first_name','last_name','email']