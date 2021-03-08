from django.shortcuts import render
from .models import Product
from .forms import ProductForm

# Create your views here.
def productDetailView(request):
    obj = Product.objects.all()
    context = {
        "products": obj,
    }
    return render(request, "product/detail.html", context)

# Create your views here.
def productCreateView(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        "form": form,
    }
    return render(request, "product/product-create.html", context)

def productDeleteView(request, id):
    obj = Product.objects.get(id = id)
    # post request
    obj.delete()
    context = {
        "object": obj,
    }
    return render(request, "product/product-delete.html", context)