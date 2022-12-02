from django.test import TestCase


class TestDjango(TestCase):

    # test if 1 == 1
    def test_this_thing_works(self):
        self.assertEqual(1, 1)

    # test if 1 == 3
    def test_this_thing_works2(self):
        self.assertEqual(1, 3)

    # test if 1 == syntax error
    def test_this_thing_works3(self):
        self.assertEqual(1, )

    # test if 1 == 4
    def test_this_thing_works4(self):
        self.assertEqual(1, 4)
