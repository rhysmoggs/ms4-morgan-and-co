from django.contrib import admin
from .models import Product, Category, Room, Special


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'room',
        'special',
        'price',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class SpecialAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Special, SpecialAdmin)
