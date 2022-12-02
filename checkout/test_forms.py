from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):
    """
    Test to see if Order Form is working
    """
    def test_full_name_is_required(self):
        """
        Test if form submits without full_name field populated
        """
        form = OrderForm({
            'full_name': '',
            'email': 'test@test.com',
            'phone_number': '1234567890',
            'street_address1': '12345th Street',
            'street_address2': 'test',
            'town_or_city': 'Anytown',
            'postcode': '12345',
            'country': 'GB',
            'county': 'test',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(
            form.errors['full_name'][0], 'This field is required.')

    def test_email_is_required(self):
        """
        Test if form submits without email field populated
        """
        form = OrderForm({
            'full_name': 'test',
            'email': '',
            'phone_number': '1234567890',
            'street_address1': '12345th Street',
            'street_address2': 'test',
            'town_or_city': 'Anytown',
            'postcode': '12345',
            'country': 'GB',
            'county': 'test',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(
            form.errors['email'][0], 'This field is required.')

    def test_phone_number_is_required(self):
        """
        Test if form submits without phone_number field populated
        """
        form = OrderForm({
            'full_name': 'test',
            'email': 'test@test.com',
            'phone_number': '',
            'street_address1': '12345th Street',
            'street_address2': 'test',
            'town_or_city': 'Anytown',
            'postcode': '12345',
            'country': 'GB',
            'county': 'test',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(
            form.errors['phone_number'][0], 'This field is required.')

    def test_street_address1_is_required(self):
        """
        Test if form submits without street_address1 field populated
        """
        form = OrderForm({
            'full_name': 'test',
            'email': 'test@test.com',
            'phone_number': '1234567890',
            'street_address1': '',
            'street_address2': 'test',
            'town_or_city': 'Anytown',
            'postcode': '12345',
            'country': 'GB',
            'county': 'test',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(
            form.errors['street_address1'][0], 'This field is required.')

    def test_town_or_city_is_required(self):
        """
        Test if form submits without town_or_city field populated
        """
        form = OrderForm({
            'full_name': 'test',
            'email': 'test@test.com',
            'phone_number': '1234567890',
            'street_address1': '12345th Street',
            'street_address2': 'test',
            'town_or_city': '',
            'postcode': '12345',
            'country': 'GB',
            'county': 'test',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(
            form.errors['town_or_city'][0], 'This field is required.')

    def test_country_is_required(self):
        """
        Test if form submits without country field populated
        """
        form = OrderForm({
            'full_name': 'test',
            'email': 'test@test.com',
            'phone_number': '1234567890',
            'street_address1': '12345th Street',
            'street_address2': 'test',
            'town_or_city': 'Anytown',
            'postcode': '12345',
            'country': '',
            'county': 'test',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(
            form.errors['country'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test if the fields visible to the users on the form are correct
        """
        form = OrderForm()
        self.assertEqual(form.Meta.fields, (
            'full_name', 'email', 'phone_number',
            'street_address1', 'street_address2',
            'town_or_city', 'postcode', 'country',
            'county',
        ))
