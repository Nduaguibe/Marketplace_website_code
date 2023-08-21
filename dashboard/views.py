from django.shortcuts import render,get_object_or_404
from items.models import item

def book_view(request,id):
    books=get_object_or_404(item,category="Books",id=id)
    return render(request,'dashboard/book_view.html',{
        'books':books
        })

def phone_view(request):
    return render(request,'dashboard/phones_view.html',{})

def toy_view(request):
    return render(request,'dashboard/toy_view.html',{})    

