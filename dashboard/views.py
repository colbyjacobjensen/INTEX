from collections import UserDict
from django.shortcuts import render, redirect
from dashboard.models import Profile
from .forms import FoodForm, UserMetricsForm
from .forms import RegisterUserForm#, UserUpdateForm, ProfileUpdateForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import IntegrityError
from django.db import transaction
from django.contrib.auth.models import User
#from .models import Food
#from .models import User
from . import urls
 
# Create your views here.

def dashboardPageView(request) :
    data = 'Data'

    context = {
        "record" : data
    }
    return render(request, 'dashboard/index.html', context)

def chartsPageView(request) :
    return render(request, 'dashboard/charts.html')

def journalPageView(request) :
    return render(request, 'dashboard/journal.html')
 
def indexPageView(request):
    # data = Food.objects.all()
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FoodForm()
    context = {
        # 'data': data,
        'form': form,
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
            messages.success(request, ("Registration successful!"))

            return redirect('metrics')
    else:
        form = RegisterUserForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/register.html', context)

# def UserMetricsPageView(request, user_id):
#     if request.method == 'POST':


#         user = User.objects.get(pk=user_id)
#         user.profile.gender = request.POST['gender']
#         user.profile.height_inches = request.POST['height_inches']
#         user.profile.weight = request.POST['weight']
#         user.profile.age = request.POST['age']
#         user.save()

# @login_required
# @transaction.atomic
# def UserMetricsPageView(request):
#     if request.method == 'POST':
#         user_form = RegisterUserForm(request.POST, instance=request.user)
#         profile_form = UserMetricsForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, ('Your profile was successfully updated!'))
#             return redirect('dashboard')
#         else:
#             messages.error(request, ('Please correct the error below.'))
#     else:
#         user_form = RegisterUserForm(instance=request.user)
#         profile_form = UserMetricsForm(instance=request.user.profile)
#     return render(request, 'dashboard/metrics.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })


            # user = form.save()
            # user.refresh_from_db()  # load the profile instance created by the signal
            # p_reg_form = ProfileRegisterForm(request.POST, instance=user.profile)
            # p_reg_form.full_clean()
            # p_reg_form.save()

def UserMetricsPageView(request) :
    if request.method == 'POST':
        user_metrics = UserMetricsForm(request.POST)
        if user_metrics.is_valid():

            # user = metrics_form.save()
            # user.refresh_from_db()  # load the profile instance created by the signal

            # metrics_form.save()

            user_data = Profile()
            user = User()
            user_id = user.pk
            user.save()

            user_data.gender = request.POST['gender']
            user_data.height_inches = request.POST['height_inches']
            user_data.weight = request.POST['weight']
            user_data.age = request.POST['age']
            user_data.user = user

            user_data.save()
            # user_metrics.gender = request.POST['gender']
            # user_metrics.height_inches = request.POST['height_inches']
            # user_metrics.weight = request.POST['weight']
            # user_metrics.age = request.POST['age']

            # user_metrics = UserMetricsForm(request.POST, instance=user.profile)
            # user_metrics.full_clean()
            # user_metrics.save()
            messages.success(request, ("Registration successful!"))
            return redirect('dashboard')
    else:
        user_metrics = UserMetricsForm()
    context = {
        'user_metrics': user_metrics
    }
    return render(request, 'dashboard/metrics.html', context)

# def register(request):
#     p_reg_form = UserMetricsForm(request.POST)
#     if form.is_valid() and p_reg_form.is_valid():
#         user = form.save()
#         user.refresh_from_db()  # load the profile instance created by the signal
#         p_reg_form = ProfileRegisterForm(request.POST, instance=user.profile)
#         p_reg_form.full_clean()
#         p_reg_form.save()
#         messages.success(request, f'Your account has been sent for approval!')
#         return redirect('login')
#     else:
#         form = UserMetricsForm()
#         p_reg_form = ProfileRegisterForm()
#     context = {
#         'form': form,
#         'p_reg_form': p_reg_form
#     }
#     return render(request, 'users/register.html', context)

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f'Your profile has been updated')
#             return redirect('profile')
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)

#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#     }

#     return render(request, 'users/profile.html', context)


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
            #  return render(request, 'login.html', {
    #             'message': 'Invalid username and/or password.',
    #             'categories': FoodCategory.objects.all()
    #         })
    else:
        return render(request, 'dashboard/login.html')

def LogoutPageView(request):
    logout(request)
    messages.success(request, ("You were successfully logged out."))
    return redirect('login')

# @login_required
# def food_log_view(request):
#     '''
#     It allows the user to select food items and 
#     add them to their food log
#     '''
#     if request.method == 'POST':
#         foods = Food.objects.all()

#         # get the food item selected by the user
#         food = request.POST['food_consumed']
#         food_consumed = Food.objects.get(food_name=food)

#         # get the currently logged in user
#         user = request.user
        
#         # add selected food to the food log
#         food_log = FoodLog(user=user, food_consumed=food_consumed)
#         food_log.save()

#     else: # GET method
#         foods = Food.objects.all()
        
#     # get the food log of the logged in user
#     user_food_log = FoodLog.objects.filter(user=request.user)
    
#     return render(request, 'food_log.html', {
#         'categories': FoodCategory.objects.all(),
#         'foods': foods,
#         'user_food_log': user_food_log
#     })


# @login_required
# def food_log_delete(request, food_id):
#     '''
#     It allows the user to delete food items from their food log
#     '''
#     # get the food log of the logged in user
#     food_consumed = FoodLog.objects.filter(id=food_id)

#     if request.method == 'POST':
#         food_consumed.delete()
#         return redirect('food_log')
    
#     return render(request, 'food_log_delete.html', {
#         'categories': FoodCategory.objects.all()
#     })