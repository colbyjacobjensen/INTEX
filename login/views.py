from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def LoginPageView(request) :
    return render(request, 'login/login.html')

def RegisterPageView(request) :
    return render(request, 'login/register.html')