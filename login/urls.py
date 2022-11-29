from django.urls import path
from .views import RegisterPageView
from .views import LoginPageView

 
urlpatterns = [
    path('login/', LoginPageView, name='login'),
    path('', RegisterPageView, name='register'),
]