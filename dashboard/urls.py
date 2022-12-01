from django.urls import path
from .views import dashboardPageView
from .views import indexPageView
from .views import chartsPageView
from .views import journalPageView
from .views import RegisterPageView
from .views import LoginPageView
from .views import LogoutPageView
from .views import UserMetricsPageView
from .views import food_log_delete


urlpatterns = [
    path('journal/', journalPageView, name='journal'),
    path('charts/', chartsPageView, name='charts'),
    path('index/', indexPageView, name='index'),
    path('dashboard/', dashboardPageView, name='dashboard'),
    path('login/', LoginPageView, name='login'),
    path('logout/', LogoutPageView, name='logout'),
    path('metrics/', UserMetricsPageView, name='metrics'),
    path('food/foodlog/delete/<int:food_id>', food_log_delete, name='food_log_delete'),
    path('', RegisterPageView, name='register'),
]