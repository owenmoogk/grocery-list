from django import forms
from .models import Item

# form for a new item
class ItemForm(forms.ModelForm):
    # overwriting the meta
    title = forms.CharField()
    description = forms.CharField(
        required = False, 
        widget=forms.Textarea(
            attrs={
                "rows": 5,
            }
        )
    )
    price = forms.DecimalField(
        required = False
    )

    class Meta:
        model = Item
        fields = [
            "title",
            "description",
            "price",
        ]