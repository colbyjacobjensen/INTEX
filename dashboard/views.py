from django.shortcuts import render, redirect
from .forms import FoodForm
from .forms import RegisterUserForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import IntegrityError
#from .models import Food
#from .models import User
from . import urls
 
# Create your views here.

def dashboardPageView(request) :
    return render(request, 'dashboard/index.html')

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
            return redirect('dashboard')
    else:
        form = RegisterUserForm()
    return render(request, 'dashboard/register.html', {
        'form':form,
        })


# def RegisterPageView(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']

#         # Ensure password matches confirmation
#         password = request.POST['password']
#         confirmation = request.POST['confirmation']
#         if password != confirmation:
#             return render(request, 'dashboard/register.html', {
#                 'message': 'Passwords must match.',
#             })

#         # Attempt to create new user
#         try:
#             user = User.objects.create_user(username, email, password)
#             user.save()
#         except IntegrityError:
#             return render(request, 'dashboard/register.html', {
#                 'message': 'Username already taken.',
#             })
#         login(request, user)

#         return HttpResponseRedirect(reverse('dashboard/index'))
#     else:
#        return render(request, 'dashboard/register.html', {
#            'categories': "none"
#        })

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
