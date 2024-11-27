from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import os
from health_calculator import models
from .models import Prediction
# ML model
import joblib
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'


# Model Load
loaded_preprocessor = joblib.load('../model/preprocessor.pkl')
health_model = joblib.load('../model/model.pkl')


# The @login_required means only logged users can access this view
@login_required
def index(request):
    predictions = Prediction.objects.filter(user=request.user)
    # Handle CRUD
    if request.method == "POST":
        if "delete" in request.POST:
            pk = request.POST.get("delete")
            return HttpResponse("clicked delet butn")

    return render(request, 'index.html', {'predictions':predictions})

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

def model_predict(request):
    if request.method == "POST":
        sex = request.POST['sex']
        age = int(request.POST["age"])
        region = request.POST['region']
        children = request.POST['children']
        smoker = request.POST['smoker']
        bmi = float(request.POST['bmi'])


        user_input = {
        "sex": sex, 
        "age": age, 
        "region": region, 
        "children": children, 
        "smoker": smoker,
        "bmi": bmi      
        }

        new_data = pd.DataFrame([user_input])

        try:
            # Pré-processar os dados com o pré-processador salvo
            processed_data = loaded_preprocessor.transform(new_data)    

            # Fazer a previsão com o modelo treinado
            predicted_cost = health_model.predict(processed_data)
            predicted_cost = round(float(predicted_cost[0][0]), 2)

        except Exception as e:
            return render(request, "index.html", {"error_message": f"Prediction error: {str(e)}"})

        # saving into the databse
        Prediction.objects.create(
            sex=sex,
            age=age,
            region=region,
            children=children,
            smoker=smoker,
            bmi=bmi,
            predicted_cost=predicted_cost,
            user=request.user
        )

        # Filtra os resultados por usuário
        predictions = Prediction.objects.filter(user=request.user)
        return render(request, 'index.html', {'prediction': predicted_cost, "predictions":predictions})


def user_logout(request):
    logout(request)
    return redirect('/')

@login_required    
def clear_database(request):
    Prediction.objects.all().delete()  # Delete data
    return redirect("/")