from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,"login.html")

def usertype(request):
    return render(request,"usertype.html")

def signup_consumer(request):
    return render(request,"signup_consumer.html")