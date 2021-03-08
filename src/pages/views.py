from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homeView(request, *args, **kwargs):
    return render(request, "home.html", {})

def contactView(request, *args, **kwargs):
    return render(request, "contact.html", {})

def aboutView(request, *args, **kwargs):
    myContext = {
        "myText": "this is about us",
        "myNumber": 123,
        "myList": [1,2,3,4,5,"GE"],
    }
    return render(request, "about.html", myContext)

def socialView(request, *args, **kwargs):
    return render(request, "social.html", {})