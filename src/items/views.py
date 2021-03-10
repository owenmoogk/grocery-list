from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Item
from .forms import ItemForm

# displaying the items that the user owns, to the user
@login_required
def itemsDetailView(request):
    
    # deletion
    if request.method == "POST":
        obj = Item.objects.get(id = request.POST.get("id"))
        obj.delete()
    
    obj = Item.objects.filter(owner = request.user)
    context = {
        "items": obj,
    }
    return render(request, "item/item-detail.html", context)

# for the user to create items
@login_required
def itemCreateView(request):
    form = ItemForm(request.POST)
    if form.is_valid():
        event = form.save(commit=False)
        event.owner = request.user
        event.save()
        form = ItemForm()
    context = {
        "form": form,
    }
    return render(request, "item/item-create.html", context)

# admin, showing all items across all users
@user_passes_test(lambda user: user.is_superuser)
def itemAllView(request):
    if request.method == "POST":
        obj = Item.objects.get(id = request.POST.get("id"))
        obj.delete()
    
    obj = Item.objects.all()
    context = {
        "items": obj,
    }
    return render(request, "item/all-items.html", context)