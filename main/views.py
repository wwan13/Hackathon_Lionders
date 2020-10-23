from django.shortcuts import render,redirect,get_object_or_404
from order import models as ordermodel
from users import models as usermodel

# Create your views here.
def home(request):
    return render(request,"index.html")

def on_going(request):
    return render(request,"on_going.html")

def detail(request):
    return render(request,"detail.html")

def my_page_lionders(request):
    return render(request,"my_page_lionders.html")
  
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

def mypage(request):
    if request.user.usertype=="consumer":
        user = get_object_or_404(usermodel.Consumer_Users,pk = request.user.id)
        return render(request,"my_page_user.html",{'user':user})
    elif request.user.usertype=="lionders":
        user = get_object_or_404(usermodel.Lionders_Users,pk = request.user.id)
        return render(request,"my_page_lionders.html",{'user':user})
    else:
        redirect('home')
    