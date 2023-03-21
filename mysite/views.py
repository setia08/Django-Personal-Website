from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Details,Projects
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request,"mysite_file/index.html")

def about(request):
    return render(request,"mysite_file/about.html")

def contact(request):
    if request.method=="POST":
        name=request.POST["name"]
        phone=request.POST["phone"]
        email=request.POST["email"]
        description=request.POST["description"]
        Details.objects.create(name=name,phone=phone,email=email,description=description)
        return render(request,"mysite_file/index.html")
    else:    
        return render(request,"mysite_file/contact.html")
    
def login_view(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index")) 
        else:
            return render(request,"mysite_file/login.html")
    else:
        return render(request,"mysite_file/login.html")

def logout_view(request):
    if request.method=="POST":
            auth.logout(request)
            return redirect('login_view')


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "mysite_file/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "mysite_file/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "mysite_file/register.html")


def client(request):
    data=Details.objects.all()
    return render(request,"mysite_file/client.html",{
        "data":data
    })

def view_project(request):
    all_projects=Projects.objects.all()
    return render(request,"mysite_file/view_projects.html",{
        "all_projects":all_projects
    })


def add_project(request):
    return render(request,"mysite_file/add_project.html")