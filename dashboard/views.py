from django.shortcuts import render,get_object_or_404
from items.models import item ,Category

    
def book_view(request,category):
    cat = get_object_or_404(Category,name=category) 
    books = item.objects.filter(category_id=cat.id)
    # books = get_object_or_404(item,category=category)
    return render(request,'dashboard/book_view.html',{'books':books})


def phone_view(request):
    return render(request,'dashboard/phones_view.html',{})

def toy_view(request):
    return render(request,'dashboard/toy_view.html',{})    





