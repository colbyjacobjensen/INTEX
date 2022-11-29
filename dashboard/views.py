from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
 
# Create your views here.
 
def index(request):
    data = User.objects.all()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserForm()
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'dashboard/dashboard.html', context)