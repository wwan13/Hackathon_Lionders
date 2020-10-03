from django.shortcuts import render,redirect
from django.contrib import auth


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
    return render(request,"signup_consumer.html")

def signup_lionders(request):
    return render(request,"signup_lionders.html")