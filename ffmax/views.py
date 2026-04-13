from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import render, redirect
from .models import User
# Create your views here.
def home(request):
    return render(request,'index.html')
def service(request):
    return render(request,'service.html')
def webdevelopment(request):
    return render(request,'web_development.html')
def graphicdesign(request):
    return render(request,'graphic_design.html')
def anime(request):
    return render(request,'anime.html')
def signup(request):
    return render(request,'signup.html')
def login(request):
    return render(request,'login.html')
def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        confirm_password = request.POST['password2']

        if password1 != confirm_password:
            return render(request, "signup.html", {"error": "Passwords do not match"})

        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {"error": "Username already exists"})

        user = User(username=username, email=email, password=password1, confirm_password=confirm_password)
        user.save()

        return redirect("login")

    return render(request, "signup.html")