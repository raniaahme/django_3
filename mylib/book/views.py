from django.shortcuts import render
from catagory.models import *
from .models import *

def List(r):
    return render(r,'book/index.html')

def Add(r):
    context={}
    context['catagories'] = Catagory.objects.all()
    if(r.method=='GET'):

        return render(r, 'book/add.html',context)
    else:
        print(r.POST)
        Book.objects.create(name=r.POST['bookname'],publisher=r.POST['bookpublisher'],catagory=Catagory.objects.get(id=r.POST['bookCatagory']))
        return render(r, 'book/add.html', context)