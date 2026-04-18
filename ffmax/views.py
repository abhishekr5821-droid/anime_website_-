from django.contrib import messages
from django.shortcuts import render, redirect
from .models import User, Anime
from django.contrib.auth import authenticate, login

# Home pages
def home(request):
    return render(request, 'index.html')

def service(request):
    return render(request, 'service.html')

def webdevelopment(request):
    return render(request, 'web_development.html')

def graphicdesign(request):
    return render(request, 'graphic_design.html')

def search(request):
    query = request.GET.get('q')

    results = []

    if query:
        q = query.lower()

        # 🔹 1. STATIC PAGE MATCHING
        pages = {
            "home": "/",
            "about": "/#about",
            "contact": "/#contact",
            "team": "/#team",
            "services": "/service",
            "anime": "/anime",
        }

        for key, url in pages.items():
            if q in key:
                return redirect(url)

        # 🔹 2. DATABASE SEARCH
        anime_results = Anime.objects.filter(title__icontains=query)

        results = anime_results

    return render(request, "search.html", {
        "query": query,
        "results": results
    })
def anime(request):
    anime_list = Anime.objects.all()

    return render(request, 'anime.html', {
        'anime_list': anime_list
    })

def logout_view(request):
    # Clear the session to log out the user
    request.session.flush()
    return redirect('home')


# LOGIN


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username, password=password)

            request.session['user_id'] = user.id
            request.session['username'] = user.username

            return redirect('home')

        except User.DoesNotExist:
            messages.error(request, "Invalid credentials")

    return render(request, 'login.html')

# SIGNUP
def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        confirm_password = request.POST['password2']    

        user = User(
            username = username,
            email = email,
            password = password,
            confirm_password = confirm_password
        )
        user.save()
        return redirect('login')        
    return render(request, 'signup.html')

    
def logout_view(request):
    # Clear the session to log out the user
    request.session.flush()
    return redirect('home')
