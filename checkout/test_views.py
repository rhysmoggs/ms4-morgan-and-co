from django.test import TestCase
from django.shortcuts import reverse

from django.contrib.messages import get_messages


class TestCheckoutViews(TestCase):
    """
    Test to see if Checkout page and process is working
    """
    def test_cache_checkout_data(self):
        """
        Test to see if cache_checkout_data is working
        """
        response = self.client.get('/checkout/cache_checkout_data/')
        self.assertEqual(response.status_code, 405)

    def test_checkout_url_exists(self):
        """
        Test to see if checkout page url exists
        """
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 302)

    def test_checkout_url_is_accessible_by_name(self):
        """
        Test to see if checkout url is accessible by name
        """
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)

    def test_checkout_url_template(self):
        """
        Test checkout uses correct template when bag is empty
        """
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/')

    def test_checkout_bag_is_empty_error(self):
        """
        Test toast Error! message appears when attempting to access /checkout/
        and bag is empty
        """
        response = self.client.get('/checkout/')
        message = list(get_messages(response.wsgi_request))
        self.assertEqual(len(message), 1)
        self.assertEqual(message[0].tags, 'error')
        self.assertEqual(
            str(message[0]), "There's nothing in your bag at the moment")
