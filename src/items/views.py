from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Item
from .forms import ItemForm
from django.http import HttpResponseRedirect

# displaying the items that the user owns, to the user
@login_required
def itemsDetailView(request):
    
    # deletion
    if request.method == "POST" and "delete" in request.POST:
        obj = Item.objects.get(id = request.POST.get("id"))
        obj.delete()
        return HttpResponseRedirect('/items')


    # to add an item
    elif request.method == "POST" and "add" in request.POST:
        form = ItemForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.owner = request.user
            event.save()
            # form = ItemForm()
        return HttpResponseRedirect('/items')

    # this will only execute on a get command
    items = Item.objects.filter(owner = request.user)
    addForm = ItemForm()

    context = {
        "items": items,
        "addForm": addForm,
    }
    return render(request, "item/item-detail.html", context)

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