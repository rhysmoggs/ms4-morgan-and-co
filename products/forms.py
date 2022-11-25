from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Room, Special


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        rooms = Room.objects.all()
        specials = Special.objects.all()
        friendly_names_category = [
            (c.id, c.get_friendly_name()) for c in categories]
        friendly_names_room = [
            (r.id, r.get_friendly_name()) for r in rooms]
        friendly_names_special = [
            (s.id, s.get_friendly_name()) for s in specials]

        self.fields['category'].choices = friendly_names_category
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        self.fields['room'].choices = friendly_names_room
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        self.fields['special'].choices = friendly_names_special
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
