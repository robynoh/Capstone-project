from django.test import TestCase
from restaurants.models import Menu

#TestCase class
class MenuItemTest(TestCase):
     def test_get_item(self):
        # Create a new instance of the Menu model
        menu_item = Menu(name="Dissert", price=10.99, description="A tasty dessert dish")

        # Assert the string representation using assertEqual
        self.assertEqual(str(menu_item), "Dissert Dish - $10.99")