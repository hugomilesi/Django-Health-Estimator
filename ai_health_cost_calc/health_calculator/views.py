from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from health_calculator import models

# The @login_required means only logged users can access this view
@login_required
def index(request):
    return render(request, 'index.html')

def user_signup(request):
    """
        This function gets the values typed in the forms inserted by the user, checks if the password and confirm-password match and them if is all True,
        it creates a user. If a matching error or else occur it will show an error message.
    """
    # Stores the values from the forms
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm-password"]

        # Checks if there is a match between passwords
        if password == confirm_password:
            try:
                # Saves the user
                user = User.objects.create_user(username, password=password)
                user.save()
                login(request, user)
                return redirect("/")
            except:
                error_message = "Error Creating Account"
                return render(request, "signup.html", {'error_message': error_message})
        else:
            error_message = "Passwords Doesn`t match"
            return render(request, "signup.html", {'error_message': error_message})
        
    return render(request, 'signup.html' )

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password =request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            error_message = "Invalid Username or Password. Please try again."
            return render(request, "login.html", {"error_message":error_message})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('/')
