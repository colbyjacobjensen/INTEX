from django.urls import path
from .views import dashboardPageView
from .views import indexPageView
from .views import chartsPageView
from .views import journalPageView
from .views import RegisterPageView
from .views import LoginPageView
from .views import LogoutPageView
from .views import UserMetricsPageView

 
urlpatterns = [
    path('journal/', journalPageView, name='journal'),
    path('charts/', chartsPageView, name='charts'),
    path('index/', indexPageView, name='index'),
    path('dashboard/', dashboardPageView, name='dashboard'),
    path('login/', LoginPageView, name='login'),
    path('logout/', LogoutPageView, name='logout'),
    path('metrics/', UserMetricsPageView, name='metrics'),
    path('', RegisterPageView, name='register'),
]