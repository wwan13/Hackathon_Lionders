from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import auth
from .models import Lionders_Users, Consumer_Users
from users import models as usermodel


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return redirect('login_fail')
    else:
        return render(request, 'login.html')


def login_fail(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return redirect('login_fail')
    else:
        return render(request, 'login_fail.html')


def usertype(request):
    return render(request,"usertype.html")


def signup_consumer(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            user = Consumer_Users.objects.create_user(
                username=request.POST['username'], 
                password=request.POST['password'],
                usertype=request.POST['usertype'],
                name=request.POST['name'],
                address_num=request.POST['address_num'],
                address_road=request.POST['address_road'],
                address_detail=request.POST['address_detail'],
                phone=request.POST['phone'])
            auth.login(request, user)
            return redirect('login')
    return render(request, 'signup_consumer.html')

def signup_lionders(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            user = Lionders_Users.objects.create_user(
                username=request.POST['username'], 
                password=request.POST['password'],
                usertype=request.POST['usertype'],
                name=request.POST['name'],
                address_num=request.POST['address_num'],
                address_road=request.POST['address_road'],
                address_detail=request.POST['address_detail'],
                phone=request.POST['phone'])
            auth.login(request, user)
            return redirect('../education')
    return render(request, 'signup_lionders.html')


def education(request):
    return render(request,'education.html')


def mypage(request):
    if request.user.usertype=="consumer":
        user = get_object_or_404(usermodel.Consumer_Users,pk = request.user.id)
    elif request.user.usertype=="lionders":
        user = get_object_or_404(usermodel.Lionders_Users,pk = request.user.id)
    else:
        return redirect('home')
    return render(request,"my_page.html",{'user':user})


def update_user_info(request):
    if request.user.usertype=="consumer":
        user = get_object_or_404(usermodel.Consumer_Users,pk = request.user.id)
        if request.method=='POST':
            if 'image' in request.FILES:
                request.POST._mutable = True
                user.image = request.FILES['image']
                user.phone = request.POST['phone']
                user.address_num = request.POST['address_num']
                user.address_road = request.POST['address_road']
                user.save()
            else:
                user.image = request.user.image
                user.phone = request.POST['phone']
                user.address_num = request.POST['address_num']
                user.address_road = request.POST['address_road']
                user.save()
            return redirect("mypage")
    elif request.user.usertype=="lionders":
        user = get_object_or_404(usermodel.Lionders_Users,pk = request.user.id)
        if request.method=='POST':
            if request.FILES['image']:
                request.POST._mutable = True
                user.image = request.FILES['image']
                user.phone = request.POST['phone']
                user.address_num = request.POST['address_num']
                user.address_road = request.POST['address_road']
                user.save()
            else:
                user.image = request.user.image
                user.phone = request.POST['phone']
                user.address_num = request.POST['address_num']
                user.address_road = request.POST['address_road']
                user.save()
            return redirect("mypage")
    else:
        return redirect('home')

    return render(request,"update_user_info.html",{'user':user,})