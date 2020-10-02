from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,"login.html")

def usertype(request):
    return render(request,"usertype.html")

def signup(request):
    return render(request,"signup.html")