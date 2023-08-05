from django.shortcuts import render,redirect
from .models import item
from .forms import NewItemForm


def home(request):
    return render(request,'items/home.html')

def base(request):
    return render(request,'items/base.html')

def front_page(request):
    items = item.objects.all()
    return render(request,'items/front_page.html',{'items':items})

def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST,request.FILES)

        if form.is_valid():
            form.save(commit=False).save()
            

            return redirect('item:front_page')
    else:
        form=NewItemForm()

    return render(request,'items/Add_item.html',{
        'form':form,
        'title':'New item'})