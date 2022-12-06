from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """ ReviewForm to allow users to add reviews """
    class Meta:
        model = Review
        fields = ['review_text', 'review_rating']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholder = {
            'review_text': 'Write your review here',
        }
        labels = {
            'review_text': 'Product Review',
            'review_rating': 'Rating',
        }

        for field in self.fields:
            self.fields[field].label = labels[field]
        self.fields['review_text'].widget.attrs['placeholder'] = (
            placeholder['review_text'])
