from django.test import TestCase
from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.views.decorators.http import require_POST
# from django.contrib import messages
from django.contrib.messages import get_messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem

from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from bag.contexts import bag_contents

import stripe
import json


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
