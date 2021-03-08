from django.shortcuts import render
from .models import Item
from .forms import ItemForm

# Create your views here.
def itemsDetailView(request):
    
    # deletion
    if request.method == "POST":
        obj = Item.objects.get(id = request.POST.get("id"))
        obj.delete()
    
    obj = Item.objects.all()
    context = {
        "items": obj,
    }
    return render(request, "item/item-detail.html", context)

# Create your views here.
def itemCreateView(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ItemForm()
    context = {
        "form": form,
    }
    return render(request, "item/item-create.html", context)