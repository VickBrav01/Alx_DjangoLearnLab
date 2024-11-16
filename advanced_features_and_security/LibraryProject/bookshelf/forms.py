# ExampleForm - here we create forms
from django import forms


class ExampleForm(forms.Form):
    name = forms.CharField(label="Your name", max_length=150)
