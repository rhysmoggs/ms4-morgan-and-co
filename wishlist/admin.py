from django.contrib import admin
from .models import Wishlist


class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'date_added',
    )

    ordering = ('-date_added',)


admin.site.register(Wishlist, WishlistAdmin)
