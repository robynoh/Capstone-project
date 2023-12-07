from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Menu,Booking  # Import the model for which you want to create a serializer


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu  # Specify the model for which you are creating the serializer
        fields = '__all__'  # Use '__all__' to include all model fields in the serializer
        # Alternatively, you can specify a tuple of field names if you only want to include specific fields

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking  # Specify the model for which you are creating the serializer
        fields = '__all__'  # Use '__all__' to include all model fields in the serializer
        # Alternatively, you can specify a tuple of field names if you only want to include specific fields

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']