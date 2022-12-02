from collections import UserDict
from django.db.models import Sum
from django.shortcuts import render, redirect
from dashboard.models import Profile
from .forms import FoodForm
from .forms import UserMetricsForm
from .forms import RegisterUserForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import IntegrityError
from django.db import transaction
from django.contrib.auth.models import User
from .models import Food
from .models import FoodLog
from . import urls
import requests
import random

# from .ninja import chooseFood
 
# Create your views here.


def dashboardPageView(request) :

    if request.method == "POST" :
        query = request.POST['food']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
        response = requests.get(api_url, headers={'X-Api-Key': 'j3WdpWFz3JI0zTDkkXXw8A==Y9P0i5ktjOjmlcOS'})

        if Food.objects.filter(foodName=query).exists() :
            database_food = Food.objects.get(foodName=query)
            foodName = database_food.foodName
            calories = database_food.calories
            fatTotal = database_food.fatTotal
            satFat = database_food.satFat
            protein = database_food.protein
            sodium = database_food.sodium
            potassium = database_food.potassium
            cholesterol = database_food.cholesterol
            carbohydrates = database_food.carbohydrates
            sugar = database_food.sugar
            phosphorus = 24
            calcium = 42
        else:
            # if response.status_code == 200:
            #     messages.success(request, ("This food is not in the database"))
            #     foodName = ""
            #     calories = 0
            #     fatTotal = 0
            #     satFat = 0
            #     protein = 0
            #     sodium = 0
            #     potassium = 0
            #     cholesterol = 0
            #     carbohydrates = 0
            #     sugar = 0
            #     phosphorus = 0
            #     calcium = 0
            # else:
            foodName = response.json()[0]['name']
            calories = response.json()[0]['calories']
            fatTotal = response.json()[0]['fat_total_g']
            satFat = response.json()[0]['fat_saturated_g']
            protein = response.json()[0]['protein_g']
            sodium = response.json()[0]['sodium_mg']
            potassium = response.json()[0]['potassium_mg']
            cholesterol = response.json()[0]['cholesterol_mg']
            carbohydrates = response.json()[0]['carbohydrates_total_g']
            sugar = response.json()[0]['sugar_g']
            phosphorus = 24
            calcium = 42

        current_user = request.user
        user_id = current_user.id
        profile = Profile.objects.get(user=user_id)

        sodiumGoalTotal = 1800
        potassiumGoalTotal = 2750
        sugarGoalTotal = 20
        proteinGoalTotal = (profile.weight / 2.20462) * .6
        proteinGoalTotal = 50
        # this is just a placeholder if we can't figure it out based on weight

        calorieGoalTotal = 2500
        fatGoalTotal = int(calorieGoalTotal * .35)
        carbGoalTotal = 1000
        phosphorusGoalTotal = 800
        calciumGoalTotal = 1800

        #goal variables percentage
        sodiumGoal = str(int(round(((sodium/sodiumGoalTotal) * 100),0))) + '%'
        potassiumGoal = str(int(round(((potassium/potassiumGoalTotal) * 100),0))) + '%'
        sugarGoal = str(int(round(((sugar/sugarGoalTotal) * 100),0))) + '%'
        proteinGoal = str(int(round(((protein/proteinGoalTotal) * 100), 0))) + '%'
        fatGoal = str(int(((fatTotal/fatGoalTotal) * 100))) + '%'
        carbGoal = str(int(round(((carbohydrates/carbGoalTotal) * 100),0))) + '%'
        calorieGoal = str(int(round(((calories/calorieGoalTotal) * 100),0))) + '%'
        phosphorusGoal = str(int(round(((phosphorus/phosphorusGoalTotal) * 100),0))) + '%'
        calciumGoal = str(int(round(((calcium/calciumGoalTotal) * 100),0))) + '%'

        #goal variables number
        sodiumGoalNum = int(round(((sodium/sodiumGoalTotal) * 100),0))
        potassiumGoalNum = int(round(((potassium/potassiumGoalTotal) * 100),0))
        sugarGoalNum = int(round(((sugar/sugarGoalTotal) * 100),0))
        proteinGoalNum = int(round(((protein/proteinGoalTotal) * 100),0))
        fatGoalNum = int(round(((fatTotal/fatGoalTotal) * 100),0))
        carbGoalNum = int(round(((carbohydrates/carbGoalTotal) * 100),0))
        calorieGoalNum = int(round(((calories/proteinGoalTotal) * 100),0))
        phosphorusGoalNum = int(round(((phosphorus/phosphorusGoalTotal) * 100),0))
        calciumGoalNum = int(round(((calcium/calciumGoalTotal) * 100),0))
        
        #remain variables
        sodiumRemain = sodiumGoalTotal - sodium
        if sodiumRemain < 0:
            sodiumRemain = 0
        potassiumRemain = potassiumGoalTotal - potassium
        if potassiumRemain < 0:
            potassiumRemain = 0
        sugarRemain = sugarGoalTotal - sugar
        if sugarRemain < 0:
            sugarRemain = 0
        proteinRemain = proteinGoalTotal - protein
        if proteinRemain < 0:
            proteinRemain = 0
        fatRemain = fatGoalTotal - fatTotal
        if fatRemain < 0:
            fatRemain = 0
        carbsRemain = carbGoalTotal - carbohydrates
        if carbsRemain < 0:
            carbsRemain = 0
        calorieRemain = calorieGoalTotal - calories
        if calorieRemain < 0:
            calorieRemain = 0

        # messages logic based on user limits
        if potassiumGoalNum > 100:
            messages.success(request, ("This food has too much potassium! Limit your potassium intake for the rest of the day."))
        if sodiumGoalNum > 100:
            messages.success(request, ("This food has too much sodium! Limit your sodium intake for the rest of the day."))
        if sugarGoalNum > 100:
            messages.success(request, ("This food has too much sugar! Limit your sugar intake for the rest of the day."))
        if proteinGoalNum > 100:
            messages.success(request, ("This food has too much protein! Limit your protein intake for the rest of the day."))
        if fatGoalNum > 100:
            messages.success(request, ("This food has too much fat! Limit your fat intake for the rest of the day."))
        if carbGoalNum > 100:
            messages.success(request, ("This food has too many carbohydrates! Limit your carbohydrate intake for the rest of the day."))
        if calories > (calorieGoalTotal / 2):
            messages.success(request, ("This food is " + str(calorieGoal) + " of your daily calories! Try eating something with fewer calories."))
        if sodium > (sodiumGoalTotal / 4):
            items = list(Food.objects.filter(sodium__lt = (sodiumGoalTotal / 10)))
            random_sodium = random.choice(items)
            messages.success(request, ("This food is " + str(sodiumGoal) + " of your daily sodium! We recommend trying something with less sodium, such as " + str(random_sodium.foodName) + "."))
        if potassium > (potassiumGoalTotal / 4):
            items = list(Food.objects.filter(potassium__lt = (potassiumGoalTotal / 10)))
            random_potassium = random.choice(items)
            messages.success(request, ("This food is " + str(potassiumGoal) + " of your daily potassium! We recommend trying something with less potassium, such as " + str(random_potassium.foodName) + "."))


        food_info = [
            'Food Name: ' + foodName.capitalize(), 
            'Calories: ' + str(calories), 
            'FatTotal: '+ str(fatTotal),
            'SatFat: ' + str(satFat),
            'Protein: '+ str(protein),
            'Sodium: '+ str(sodium),
            'Potassium: '+ str(potassium),
            'Cholesterol: '+ str(cholesterol),
            'Carbohydrates: '+ str(carbohydrates),
            'Sugar: '+ str(sugar) 
        ]

        context = {
            'foodName': foodName,
            'calories': calories,
            'fatTotal': fatTotal,
            'satFat': satFat,
            'protein': protein,
            'sodium': sodium,
            'potassium': potassium,
            'cholesterol': cholesterol,
            'carbohydrates': carbohydrates,
            'sugar': sugar,
            'library':food_info,
            'sodiumGoal': sodiumGoal,
            'potassiumGoal': potassiumGoal,
            'sodiumGoalNum': sodiumGoalNum,
            'potassiumGoalNum': potassiumGoalNum,
            'sugarGoal': sugarGoal,
            'sugarGoalNum': sugarGoalNum,
            'proteinGoal': proteinGoal,
            'proteinGoalNum': proteinGoalNum,
            'fatGoal': fatGoal,
            'fatGoalNum': fatGoalNum,
            'carbGoal': carbGoal,
            'carbGoalNum': carbGoalNum,
            'carbGoalTotal': carbGoalTotal,
            'carbsRemain': carbsRemain,
            'calorieGoal': calorieGoal,
            'calorieGoalNum': calorieGoalNum,
            'calorieRemain': calorieRemain,
            'proteinRemain': proteinRemain,
            'fatRemain': fatRemain,
            'sodiumRemain': sodiumRemain,
            'potassiumRemain': potassiumRemain,
            'sugarRemain': sugarRemain,
            'phosphorus': phosphorus,
            'phosphorusGoal': phosphorusGoal,
            'phosphorusGoalNum': phosphorusGoalNum,
            'phosphorusGoalTotal': phosphorusGoalTotal,
            'calcium': calcium,
            'calciumGoal': calciumGoal,
            'calciumGoalNum': calciumGoalNum,
            'calciumGoalTotal': calciumGoalTotal

        }
        if response.status_code == requests.codes.ok:
            return render(request, 'dashboard/index.html', context)
        else:
            return ("Error:", response.status_code, response.text)

    return render(request, 'dashboard/index.html')

@login_required
def FoodLogDeletePageView(request, food_id):
    '''
    It allows the user to delete food items from their food log
    '''
    # get the food log of the logged in user
    food_consumed = FoodLog.objects.filter(id=food_id)

    if request.method == 'POST':
        food_consumed.delete()
        return redirect('journal')
    
    
    return render(request, 'dashboard/food_log_delete.html')

def deleteFoodPageView(request, food_id) :
    data = Food.objects.get(id=food_id)

    data.delete()

    return journalPageView(request)


def journalPageView(request) :
    #everything is in grams, sodium, potassium, cholestoral in mg

    sodiumGoalTotal = 1800
    potassiumGoalTotal = 2750
    phosphorusGoalTotal = 800
    calciumGoalTotal = 1800
    calorieGoalTotal = 2500

    '''
    It allows the user to select food items and 
    add them to their food log
    '''
    if request.method == 'POST':

        query = request.POST['food']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query.lower())
        response = requests.get(api_url, headers={'X-Api-Key': 'j3WdpWFz3JI0zTDkkXXw8A==Y9P0i5ktjOjmlcOS'})

        if Food.objects.filter(foodName=query).exists() :
            database_food = Food.objects.get(foodName=query)
            foodName = database_food.foodName
            calories = database_food.calories
            fatTotal = database_food.fatTotal
            satFat = database_food.satFat
            protein = database_food.protein
            sodium = database_food.sodium
            potassium = database_food.potassium
            cholesterol = database_food.cholesterol
            carbohydrates = database_food.carbohydrates
            sugar = database_food.sugar
            phosphorus = 501
            calcium = 120
        else:
            # if response.status_code == 200:
            #     messages.success(request, ("This food is not in the database"))
            #     foodName = ""
            #     calories = 0
            #     fatTotal = 0
            #     satFat = 0
            #     protein = 0
            #     sodium = 0
            #     potassium = 0
            #     cholesterol = 0
            #     carbohydrates = 0
            #     sugar = 0
            #     phosphorus = 0
            #     calcium = 0
            # else:
            foodName = response.json()[0]['name']
            calories = response.json()[0]['calories']
            fatTotal = response.json()[0]['fat_total_g']
            satFat = response.json()[0]['fat_saturated_g']
            protein = response.json()[0]['protein_g']
            sodium = response.json()[0]['sodium_mg']
            potassium = response.json()[0]['potassium_mg']
            cholesterol = response.json()[0]['cholesterol_mg']
            carbohydrates = response.json()[0]['carbohydrates_total_g']
            sugar = response.json()[0]['sugar_g']
            phosphorus = 642
            calcium = 1430

        current_user = request.user
        user_id = current_user.id
        profile = Profile.objects.get(user=user_id)

        sodiumGoalTotal = 1800
        potassiumGoalTotal = 2750
        sugarGoalTotal = 20
        proteinGoalTotal = (profile.weight / 2.20462) * .6
        # proteinGoalTotal = 50
        # this is just a placeholder if we can't figure it out based on weight
        calorieGoalTotal = 2500
        fatGoalTotal = calorieGoalTotal * .35
        carbGoalTotal = 1000
        phosphorusGoalTotal = 800
        calciumGoalTotal = 1800

        if not Food.objects.filter(foodName=foodName).exists():

            foodObject = Food()
            
            foodObject.foodName = foodName
            foodObject.calories = calories
            foodObject.fatTotal = fatTotal
            foodObject.satFat = satFat
            foodObject.protein = protein
            foodObject.sodium = sodium
            foodObject.potassium = potassium
            foodObject.cholesterol = cholesterol
            foodObject.carbohydrates = carbohydrates
            foodObject.sugar = sugar

            foodObject.save()
        
        foods = Food.objects.all()

        # get the food item selected by the user
        food = foodName
        food_consumed = Food.objects.get(foodName=food)

        # get the currently logged in user
        user = request.user
        
        # add selected food to the food log
        food_log = FoodLog(user=user, food_consumed=food_consumed)
        food_log.save()
    

    else: # GET method
        foods = Food.objects.all()
        
    # get the food log of the logged in user
    user_food_log = FoodLog.objects.filter(user=request.user)
    
    # query returning the sum of sodium and potassium
    total_sodium_query = FoodLog.objects.aggregate(sodium_sum=Sum('food_consumed__sodium'))
    total_potassium_query = FoodLog.objects.aggregate(potassium_sum=Sum('food_consumed__potassium'))

    #checks if logged in user is a new user
    if (total_sodium_query['sodium_sum'] == None) and (total_potassium_query['potassium_sum'] == None):
        sodiumPercent = 0
        potassiumPercent = 0
        messages.success(request, ("Add food to your food log to see your daily nutrient totals!"))
    else:
        sodiumPercent = int(round(((total_sodium_query['sodium_sum']/sodiumGoalTotal) * 100),0))
        potassiumPercent = int(round(((total_potassium_query['potassium_sum']/potassiumGoalTotal) * 100),0))

        if total_sodium_query['sodium_sum'] > sodiumGoalTotal:
            sodiumExceed = total_sodium_query['sodium_sum'] - sodiumGoalTotal
            messages.success(request, ("You have exceeded your sodium recommendation for the day by " + str(sodiumExceed) + ". Limit your sodium intake for the rest of the day."))

            items = list(Food.objects.filter(sodium__lt = (sodiumGoalTotal / 25)))
            random_sodium = random.sample(items, 3)
            messages.success(request, ("We recommend trying some of the following foods with less sodium, such as " + str(random_sodium[0]) + ", " + str(random_sodium[1]) + " or " + str(random_sodium[2])))
    
        if total_potassium_query['potassium_sum'] > potassiumGoalTotal:
            potassiumExceed = total_potassium_query['potassium_sum'] - potassiumGoalTotal
            messages.success(request, ("You have exceeded your potassium recommendation for the day by " + str(potassiumExceed) + ". Limit your potassium intake for the rest of the day."))
            
            items = list(Food.objects.filter(potassium__lt = (potassiumGoalTotal / 25)))
            random_potassium = random.sample(items, 3)
            messages.success(request, ("We recommend trying some of the following foods with less potassium, such as " + str(random_potassium[0]) + ", " + str(random_potassium[1]) + " or " + str(random_potassium[2])))

    # hard coded values for now until we get a new API that includes these
    calciumPercent = 34
    phosphorusPercent = 12


    context = {
        'foods': foods,
        'user_food_log': user_food_log,
        'calciumPercent': calciumPercent,
        'potassiumPercent': potassiumPercent,
        'phosphorusPercent': phosphorusPercent,
        'sodiumPercent': sodiumPercent,
        'calorieGoalTotal': calorieGoalTotal
    }
    return render(request, 'dashboard/journal.html', context)


 

def indexPageView(request):
    # data = Food.objects.all()
    user=request.user
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FoodForm()
    context = {
        'user': user,
        'form': form
    }
    return render(request, 'dashboard/index.html', context)

def RegisterPageView(request) :
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('metrics')
    else:
        form = RegisterUserForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/register.html', context)

def UserMetricsPageView(request) :
    if request.method == 'POST':
        user_metrics = UserMetricsForm(request.POST)
        if user_metrics.is_valid():

            user_data = Profile()
            user = request.user
            user_id = user.pk

            user_data.gender = request.POST['gender']
            user_data.height_inches = request.POST['height_inches']
            user_data.weight = request.POST['weight']
            user_data.age = request.POST['age']
            user_data.user = user

            user_data.save()

            messages.success(request, ("Registration successful!"))
            return redirect('dashboard')
    else:
        user_metrics = UserMetricsForm()
    context = {
        'user_metrics': user_metrics
    }
    return render(request, 'dashboard/metrics.html', context)



def LoginPageView(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.success(request, ("There was an error logging in, try again."))
            return redirect('login')
    else:
        return render(request, 'dashboard/login.html')


# Logout page view
def LogoutPageView(request):
    logout(request)
    messages.success(request, ("You were successfully logged out."))
    return redirect('login')


# Profile page view
@login_required
def ProfilePageView(request):
    '''
    It allows the user to edit their metrics
    '''

    if request.method == 'POST':

        user = request.user
        user_profile = Profile.objects.get(user=user)

        # get the values from the form
        user_profile.gender = request.POST['gender']
        user_profile.height_inches = request.POST['height']
        user_profile.weight = request.POST['weight']
        user_profile.age = request.POST['age']

        user_profile.save()
        # messages.success(request, ("Registration successful!"))
        
        return render(request, 'dashboard/profile.html')
        
     # get the currently logged in user
    user = request.user

    # get the food item selected by the user
    user_profile = Profile.objects.get(user=user)
    gender = user_profile.gender
    height = user_profile.height_inches
    weight = user_profile.weight
    age = user_profile.age

    context = {
        'gender': gender,
        'height': height,
        'weight': weight,
        'age': age
    }
    
    return render(request, 'dashboard/profile.html', context)


# Single profile page view
def showSingleProfilePageView(request) :
    user = request.user
    profile = Profile.objects.get(user = user)

    context = {
        "profile" : profile,
    }
    return render(request, 'dashboard/profile_edit.html', context)


# Edit profile page view
@login_required
def profileEditPageView(request):
    if request.method == 'POST':
        user=request.user
        profile = Profile.objects.get(user=user)

        profile.gender = request.POST['gender']
        profile.height_inches = request.POST['height']
        profile.weight = request.POST['weight']
        profile.age = request.POST['age']

        profile.save()
        return redirect('profile')

    return ProfilePageView(request)


#Food add page view
@login_required
def foodAddPageView(request):
    '''
    It allows the user to add a new food item
    '''
    if request.method == 'POST':
        food_form = FoodForm(request.POST, request.FILES)

        if food_form.is_valid():
            new_food = food_form.save(commit=False)
            new_food.save()

            messages.success(request, ("The new food item added successfully."))

            return render(request, 'dashboard/food_add.html', {
                'food_form': FoodForm(),
            })
        
        else:
            return render(request, 'dashboard/food_add.html', {
                'food_form': FoodForm(),
            })

    else:
        return render(request, 'dashboard/food_add.html', {
            'food_form': FoodForm(),
        })