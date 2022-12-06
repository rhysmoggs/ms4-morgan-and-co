from django.test import TestCase

from products.models import Product, Category, Room, Special


class TestBagViews(TestCase):
    """
    Test the bag views work correctly
    """
    def setUp(self):
        """
        Set up test data for testing
        """
        self.category = Category.objects.create(
            name='test_category',
            friendly_name='Test Category',
        )
        self.room = Room.objects.create(
            name='test_room',
            friendly_name='Test Room',
        )
        self.special = Special.objects.create(
            name='test_special',
            friendly_name='Test Special',
        )

        self.product = Product.objects.create(
            category=self.category,
            room=self.room,
            special=self.special,
            sku='777111222',
            name='test product',
            description='test description',
            price=99.99,
        )

        self.quantity = 1

        self.item_in_bag = [{
            'product': str(self.product.id),
            'quantity': int(self.quantity),
        }]

    def test_bag_url_exists(self):
        """
        Test to see if bag page url exists
        """
        response = self.client.get('/bag/')
        self.assertTrue(response.status_code, 200)

    def test_add_to_bag_view(self):
        """
        Test that add_to_bag view works
        """
        bag_data = {
            'product': Product.objects.get(pk=self.product.id),
            'quantity': int(self.quantity),
            'redirect_url': f'/products/{self.product.id}/'
        }

        response = self.client.post(f'/bag/add/{self.product.id}/', bag_data)
        self.assertEqual(response.status_code, 302)
