from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurants.models import Menu  # Replace 'yourapp' with the actual name of your Django app
from restaurants.serializers import MenuSerializer  # Import your MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        self.menu_item1 = Menu.objects.create(name="Dish1", price=9.99, description="Description1")
        self.menu_item2 = Menu.objects.create(name="Dish2", price=12.99, description="Description2")
        # Add more instances as needed

    def test_getall(self):
        # Retrieve all Menu objects using the API endpoint
        url = reverse('menu-list')  # Assuming you have a 'menu-list' URL for listing all Menu items
        client = APIClient()
        response = client.get(url)

        # Assert that the request was successful (status code 200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Serialize the retrieved data and assert it equals the expected serialized data
        expected_data = MenuSerializer([self.menu_item1, self.menu_item2], many=True).data
        self.assertEqual(response.data, expected_data)
