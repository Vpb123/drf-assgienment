from rest_framework import serializers
from .models import UserDb

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = UserDb
        fields ='__all__'