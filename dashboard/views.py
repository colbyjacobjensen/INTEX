from django.shortcuts import render, redirect
from .forms import FoodForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Food
from .models import User
 
# Create your views here.

def dashboardPageView(request) :
    return render(request, 'dashboard/index.html')

def chartsPageView(request) :
    return render(request, 'dashboard/charts.html')

def journalPageView(request) :
    return render(request, 'dashboard/journal.html')
 
def indexPageView(request):
    data = Food.objects.all()
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FoodForm()
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'dashboard/index.html', context)

def LoginPageView(request) :
    return render(request, 'dashboard/login.html')

# def RegisterPageView(request) :
#     return render(request, 'register.html')

def RegisterPageView(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']

        # Ensure password matches confirmation
        password = request.POST['password']
        confirmation = request.POST['confirmation']
        if password != confirmation:
            return render(request, 'dashboard/register.html', {
                'message': 'Passwords must match.',
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, 'dashboard/register.html', {
                'message': 'Username already taken.',
            })
        login(request, user)

        return HttpResponseRedirect(reverse('dashboard/index'))
    else:
       return render(request, 'dashboard/register.html', {
           'categories': "none"
       })