from django.shortcuts import render, redirect
from .models import Item

# Create your views here.
def create_item(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        Item.objects.create(name=name, description=description)
        return redirect('item_list')
    return render(request,'item_form.html')

def item_list(request):
    items = Item.objects.all()
    return render(request,'item_list.html',{'items':items})



def update_item(request,id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.save()
        return redirect('item_list')
    return render(request,'item_form.html',{'item':item})


def delete_item(request,id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request,'item_confirm_delete.html',{'item':item})
