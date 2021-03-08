from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
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
        model = Product
        fields = [
            "title",
            "description",
            "price",
        ]