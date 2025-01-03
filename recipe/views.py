from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from datetime import datetime
from recipe.models import Contact1
from django.contrib import messages
import numpy as np
from .models import Recipe
import csv
from . import program  # Assuming program.py is in the same directory as views.py
from django.http import JsonResponse
import recipe.program as program
import pandas as pd
# Create your views here.
#@login_required(login_url='login')

def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        desc=request.POST.get("desc")
        contact=Contact1(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "FORM SUBMITED.THANK YOU!")
    return render(request, 'contact.html')
def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Incorrect username or password.'})

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


# Load CSV file once
recipes = pd.read_csv("recipe/data/food_data.csv")

def mood(request):
    # Clear conversation history when the page is revisited
    if request.method == 'GET':
        request.session['conversation_history'] = []

    if 'conversation_history' not in request.session:
        request.session['conversation_history'] = []

    conversation_history = request.session['conversation_history']

    if request.method == 'POST':
        user_input = request.POST.get('message')
        conversation_history.append({'user': user_input})
        bot_response = program.Mood_recipe(user_input)
        conversation_history.append({'bot': bot_response})  # Make sure bot response is correctly appended
        request.session['conversation_history'] = conversation_history

    return render(request, 'mood.html', {'conversation_history': conversation_history})

def dishname(request):
    # Clear conversation history when the page is revisited
    if request.method == 'GET':
        request.session['conversation_history'] = []

    if 'conversation_history' not in request.session:
        request.session['conversation_history'] = []

    conversation_history = request.session['conversation_history']

    if request.method == 'POST':
        user_input = request.POST.get('message')
        conversation_history.append({'user': user_input})
        bot_response = program.Dish_recipe(user_input)
        conversation_history.append({'bot': bot_response})  # Make sure bot response is correctly appended
        request.session['conversation_history'] = conversation_history

    return render(request, 'dish.html', {'conversation_history': conversation_history})



def ingredients(request):
    # Clear conversation history when the page is revisited
    if request.method == 'GET':
        request.session['conversation_history'] = []

    if 'conversation_history' not in request.session:
        request.session['conversation_history'] = []

    conversation_history = request.session['conversation_history']

    if request.method == 'POST':
        user_input = request.POST.get('message')
        conversation_history.append({'user': user_input})
        bot_response = program.Ingredient_recipe(user_input)
        conversation_history.append({'bot': bot_response})  # Make sure bot response is correctly appended
        request.session['conversation_history'] = conversation_history

    return render(request, 'ingredient.html', {'conversation_history': conversation_history})
