from django import forms


class CreateNewList(forms.Form):
    newItem = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)

class CreateNewItem(forms.Form):
    newItem = forms.CharField(label="Name", max_length=200)