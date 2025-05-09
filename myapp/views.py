from operator import truediv
import string
from urllib import request
from django.http import HttpResponse
import datetime
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login

from django.contrib import messages
from django.contrib.auth.models import User

def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, "Registration successful! Please log in.")
                return redirect('login')
            else:
                messages.error(request, "Username already exists.")
        else:
            messages.error(request, "Passwords do not match.")

    return render(request, "register.html")





def login_view(request):  # Avoid naming conflict with Django's login()
    username = "" 
    city=""
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        city=request.POST["city"]
        user = authenticate(request, username=username, password=password)  # Authenticate user

        if user is not None:
            login(request, user)  # Ensure user is passed correctly
            request.session["username"] = user.username # store the data in the  url
            request.session["city"] = city

            return redirect('home')  # Redirect after successful login
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "login.html",{'username':username,'city':city}) 


def home(request):  
    username = request.session.get("username", "Guest")  # Retrieve username from session
    city = request.session.get("city", "Unknown City")  # Default to "Unknown City" if not found
    isActive = True
    if request.method == 'POST':
        check = request.POST.get('check')  # ✅ Fix: Corrected syntax
        isActive = bool(check)  # ✅ Fix: Simplified True/False conversion
    date = datetime.datetime.now()  # Define 'date' before using it


    
  
    name = "Raj Kumar"
    
    list_of_programs = [
        'WAP to check if a number is even or odd',
        'Write a program to print "Hello World"',
        'WAP to check prime numbers',
        'WAP to print Pascal Triangle'
    ]
    
    student = {
        'student_name': "Rahul",
        'student_college': "Goel",
        'student_city': "Lucknow"
    }
    
    data = {
        'date': date,  # Now 'date' is correctly defined above
        'isActive': isActive,
        'name': name,
        'list_of_programs': list_of_programs,
        'student_data': student
    }

    print("This is the test function")
    
    return render(request, "home.html", {"username": username,"city":city,**data})


def services(request):
   # return HttpResponse("<h1>this is the about</h1>")
   return render(request,"services.html",{})


def about(request):
   # return HttpResponse("<h1>this is the about</h1>")
   return render(request,"about.html",{})
