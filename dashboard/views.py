from django.shortcuts import render,get_object_or_404
from items.models import item
'''
def finding_objects(items=item.objects.all()):
    lst = []
    books_list = []
    ctgry_list = []
    book_ctgry = []

    obj_list = list(items[0::])

    x=1
    y=5
    for i in obj_list:
        lst.append(i)

    for i in lst:
        ctgry_list.append(i.category) 
    #book_ctgry.append(ctgry_list[2])
        for i in ctgry_list:
        if i == book_ctgry:
            books_list.append(i)
    return books_list
    class objects:
        def __init__(self,obj):
            self.obj = obj

        def __eq__(self,category):
            if isinstance(category,objects):
                return self.obj == category.obj
            return False

    obj1=objects(obj_list)
    obj2=objects(ctgry_list)
    return obj1 == '''

    
        

item_ids = [num for num in range(0,100)]
def book_view(request,id_in):
    books = get_object_or_404(item,item_ids=id_in,category = 'Books')
    return render(request,'dashboard/book_view.html',{'books':books})

def phone_view(request):
    return render(request,'dashboard/phones_view.html',{})

def toy_view(request):
    return render(request,'dashboard/toy_view.html',{})    

