from django import forms

class ItemForm(forms.Form):
    content = forms.CharField(max_length=200)