from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Room


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        rooms = Room.objects.all()
        friendly_names_category = [
            (c.id, c.get_friendly_name()) for c in categories]
        friendly_names_room = [(r.id, r.get_friendly_name()) for r in rooms]

        self.fields['category'].choices = friendly_names_category
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        self.fields['room'].choices = friendly_names_room
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
