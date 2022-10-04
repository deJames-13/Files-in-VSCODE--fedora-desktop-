from django.contrib import admin
from .models import ToDoList, Item

# Register your models here.
models = [ToDoList, Item]

admin.site.register(models)