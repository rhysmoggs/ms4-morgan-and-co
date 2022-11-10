from django.db import models
from django.contrib.auth.models import User

from products.models import Product


class Review(models.Model):
    """
    Review model for user to complete
    """

    RATING = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_author = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField(max_length=250, blank=True)
    review_rating = models.IntegerField(choices=RATING, default=5, blank=False)
    review_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ displays reviews by newest first """
        ordering = ['-review_date']

    def __str__(self):
        return self.review_text
