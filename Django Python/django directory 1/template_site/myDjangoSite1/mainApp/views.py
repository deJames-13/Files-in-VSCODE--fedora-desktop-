from .models import ToDoList, Item
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect
from django.template import Template, Context
from .forms import CreateNewList, CreateNewItem
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_protect

# Create your views here.

def base(response):
    return render(response, "mainApp/base.html", {})

def home(response):
    if not response.user.is_authenticated:
        return redirect("/")        
    return render(response, "mainApp/home.html", {})

def index(response):
    return HttpResponse("<h1> Index Page </h1>")



# AJAX PAGE

def v1(response, id):
    get_info = response.POST
    t = Template(get_info['form_template'])
    print("#"*100, f"\n{get_info['form_template']}\n", "#"*100)
    
    return HttpResponse(get_info['form_template'])

# APP PAGES

def todolist(response, id=None):
    if not response.user.is_authenticated:
        return redirect("/")    
    # Basically a variable dictionary for the html templates !important
    def view_ctx(id) -> dict:  
        all_tdl = tdl.all()
        ls = tdl.all()[id-1] if id else tdl.all()
        ls_dic = {
        "id": id,
        # a very inconvenient way to calculate pages
        "page": ((id-2, "<") if id > 2 else 0, 
                 (id-1, id-1) if id > 1 else 0, 
                 (id, id), 
                 (id+1, id+1) if id < len(all_tdl) else 0, 
                 (id+2, ">") if id+1 < len(all_tdl) else 0),
        "name": ls.name,
        "items": ls.item_set.all(),  
        } if id else {"id": 0, "ls": [(ls[i], i+1) for i in range(len(ls))]}
        return ls_dic
    user = response.user
    tdl = user.todolist_set
    ls = tdl.all()[id-1] if id else tdl.all()
    # Checks if the response is POST
    if response.method == "POST":
        if response.POST.get("save"):
            for item in ls.item_set.all():
                item.complete = True if response.POST.get(f"c{item.id}") == 'clicked' else False
                item.save() 
        elif response.POST.get("add"):
            # Creates a query based on the response
            form = CreateNewItem(response.POST) if id else CreateNewList(response.POST)
            # Check the validity of the response 
            if form.is_valid():        
                n = form.cleaned_data["newItem"]
                t = ls.item_set.create(text=n, complete=False) if id else tdl.create(name=n)
                t.save()
                # instance = form.save()
                # ser_instance = serializers.serialize('json', [instance,])     
                ls_dic = view_ctx(id)
                # print("#"*100, f"\n{form}\n", "#"*100)   

    ls_dic = view_ctx(id)       
    rendered = render_to_string("mainApp/to-do-list.html", context=ls_dic, request=response) 
    # print("#"*100, f"\n{rendered}\n", "#"*100)
    return HttpResponse(rendered)
    


