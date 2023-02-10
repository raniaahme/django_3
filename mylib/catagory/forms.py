from django import forms
from .models import Catagory

class CatagoryForm(forms.Form):
    name=forms.CharField(label='Catagory_name',initial='rararrr')

