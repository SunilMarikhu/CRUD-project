from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.contrib import messages
# Create your views here.
def dashboard(request):
    return render(request, 'base.html')

def item_name(request):
    if request.method =='POST' and request.FILES:
        product = request.POST['product']
        name = request.POST['name']
        description = request.POST['description']
        file = request.FILES['file']
        price = request.POST['price']
        
        new_item = Item(product=product, name=name, description=description, image=file, price=price)
        new_item.save()
        
    Items = Item.objects.all()

    return render(request, 'home.html',{'product':Items})


def delete_item(request, id):
    item= Item.objects.get(id=id)
    item.delete()
    return redirect ('item_name')


def edit_item(request, id):
    if request.method =='POST'and request.FILES:
        item = Item.objects.get(id=id)
        item.product = request.POST['product']
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.image = request.FILES['file']
        item.price = request.POST['price']
        
        item.save()
        messages.success(request, "Product save sucessfully")
        return redirect(item_name)
    else:
        item = Item.objects.get(id=id)
    
    return render(request, 'edit.html', {'item':item})
        
    