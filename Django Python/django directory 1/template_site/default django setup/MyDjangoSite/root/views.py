from django.shortcuts import render

context = {}
# Create your views here.
def base(response):
    return render(response, "root/base.html", context)

def home(response):
    return render(response, "root/home.html", context)

def view(response):
    return render(response, "root/view.html", context)
