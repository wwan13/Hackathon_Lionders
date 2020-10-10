from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"index.html")


def detail(request):
    return render(request,"detail.html")

  
def require_login(request):
    return render(request,"require_login.html")
