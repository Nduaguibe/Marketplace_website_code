from django.shortcuts import render,redirect,get_object_or_404
from .models import item,Category
from .forms import NewItemForm


def home(request):
    return render(request,'items/home.html')

def base(request):
    return render(request,'items/base.html')

def front_page(request):
    Book=Category.objects.get(name="Books")
    Phone=Category.objects.get(name="Phones")
    Toy=Category.objects.get(name="Toys")
    return render(request,'items/front_page.html',{
        'Book':Book,
        'Phone':Phone,
        'Toy':Toy,
            })
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST,request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            

            return redirect('items:front_page')
    else:
        form=NewItemForm()

    return render(request,'items/Add_item.html',{
        'form':form,
        'title':'New item'})
    
def detail(request,id):
    categories = get_object_or_404(Category,id=id)
    return render(request,'item/detail.html',{'categories':categories})

def search_value(request):
    if request.method == 'POST':
        searched=request.POST['query']
        items = item.objects.filter(name__contains=searched)
    return render(request,'items/search_value.html',{'searched':searched,'items':items})
