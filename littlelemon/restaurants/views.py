from django.shortcuts import render
from rest_framework.decorators import api_view

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Menu  # Import your Menu model
from .serializers import MenuSerializer  # Import the serializer you created
from rest_framework import viewsets
from .models import Booking  # Import your Booking model
from .serializers import BookingSerializer  # Import the serializer you created
from rest_framework.permissions import IsAuthenticated


class MenuItemView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()  # Define the queryset for the ListCreateAPIView
    serializer_class = MenuSerializer  # Specify the serializer class for serialization

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()  # Define the queryset for the RetrieveUpdateDestroyAPIView
    serializer_class = MenuSerializer  # Specify the serializer class for serialization

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()  # Fetch all objects from the Booking model
    serializer_class = BookingSerializer  # Set the serializer class for serialization

# Create your views here.
def index(request):
    return render(request, 'index.html', {})



