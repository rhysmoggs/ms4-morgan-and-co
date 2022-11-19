from django.contrib import admin
from .models import Review

# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'review_author',
        'review_text',
        'review_rating',
        'review_date'
    )


admin.site.register(Review)
