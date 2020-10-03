from django.shortcuts import render,redirect
from django.contrib import auth
from .models import Lionders_Users, Consumer_Users


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
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

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
                address=request.POST['address'],
                phone=request.POST['phone'])
            auth.login(request, user)
            return redirect('home')
    return render(request, 'signup_consumer.html')

def signup_lionders(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            user = Lionders_Users.objects.create_user(
                username=request.POST['username'], 
                password=request.POST['password'],
                usertype=request.POST['usertype'],
                name=request.POST['name'],
                address=request.POST['address'],
                phone=request.POST['phone'])
            auth.login(request, user)
            return redirect('home')
    return render(request, 'signup_lionders.html')