from django.shortcuts import render, redirect
from .models import Food
from .forms import FoodForm
 
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