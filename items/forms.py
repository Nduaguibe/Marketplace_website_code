from django import forms
from .models import item

INPUT_CLASS= 'br-10'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = ('category','name','price','description','image','is_sold',)

       