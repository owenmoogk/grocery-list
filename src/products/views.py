from django.shortcuts import render
from .models import Product
from .forms import ProductForm

# Create your views here.
def productDetailView(request):
    
    # deletion
    if request.method == "POST":
        obj = Product.objects.get(id = request.POST.get("id"))
        obj.delete()
    
    obj = Product.objects.all()
    context = {
        "products": obj,
    }
    return render(request, "product/product-detail.html", context)

# Create your views here.
def productCreateView(request):
    # ProductForm() is a form that is made in forms.py
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        "form": form,
    }
    return render(request, "product/product-create.html", context)

# def productDeleteView(request, id):
#     obj = Product.objects.get(id = id)
#     # post request
#     obj.delete()
#     context = {
#         "object": obj,
#     }
#     return render(request, "product/product-delete.html", context)