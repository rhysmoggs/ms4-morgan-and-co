from django.test import TestCase

from .models import Order
from products.models import Product


class TestOrderModel(TestCase):
    """
    Test to see if the Order model works
    """
    @classmethod
    def setUpTestData(cls):
        Order.objects.create(
            full_name="Test McTest",
            email="test@test.com",
            phone_number="1234567890",
            street_address1="12345th Street",
            street_address2="test",
            town_or_city="Anytown",
            postcode="12345",
            country="GB",
            county="test",
        )

    def test_order_string_method_returns_order_number(self):
        """
        Test Order model string method
        """
        order_number = Order.objects.create(order_number='141414')
        self.assertEqual(str(order_number), '141414')

    def test_checkout_details(self):
        """
        Test to see that checkout fields auto-populate if user
        has saved information previously
        """
        order = Order.objects.get(id=1)
        self.assertEqual(order.full_name, 'Test McTest')
        self.assertEqual(order.email, 'test@test.com')
        self.assertEqual(order.phone_number, '1234567890')
        self.assertEqual(order.street_address1, '12345th Street')
        self.assertEqual(order.street_address2, 'test')
        self.assertEqual(order.town_or_city, 'Anytown')
        self.assertEqual(order.postcode, '12345')
        self.assertEqual(order.country, 'GB')
        self.assertEqual(order.county, 'test')


class TestOrderLineItem(TestCase):
    """
    Test to see if the OrderLineItem model works
    """
    def test_order_line_item_string_method_returns_sku_and_order_number(self):
        """
        Test OrderLineItem model string method
        """
        product = Product.objects.create(sku="777111444", price=99.99)
        order = Order.objects.create(order_number="151515")
        correct = "SKU 777111444 on order 151515"
        self.assertEqual(str(
            f'SKU {product.sku} on order {order.order_number}'), correct)
