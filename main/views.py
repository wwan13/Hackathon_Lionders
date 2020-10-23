from django.shortcuts import render,redirect,get_object_or_404
from order import models as ordermodel

# Create your views here.
def home(request):
    return render(request,"index.html")

def on_going(request):
    return render(request,"on_going.html")

def detail(request):
    return render(request,"detail.html")

  
def require_login(request):
    return render(request,"require_login.html")

def create_objs(request):
    items = ordermodel.Item.objects.all()
    return render(request,"create_objs.html",{'items':items})

def create_item_objects(requset):
    file = open('main/textfiles/items.txt', mode='rt', encoding='utf-8')
    lists = file.readlines()
    for list in lists:
        tmp = list.split(' ')
        item = ordermodel.Item(
            store = tmp[0],
            item_name = tmp[1],
            price = int(tmp[2]),
        )
        item.save()
    return redirect("create_objs")