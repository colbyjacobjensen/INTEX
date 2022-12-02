from django.urls import path
from .views import ProfilePageView, profileEditPageView, showSingleProfilePageView
from .views import dashboardPageView
from .views import indexPageView
from .views import journalPageView
from .views import RegisterPageView
from .views import LoginPageView
from .views import LogoutPageView
from .views import UserMetricsPageView
from .views import foodAddPageView
from .views import FoodLogDeletePageView

urlpatterns = [
    path('journal/', journalPageView, name='journal'),
    path('index/', indexPageView, name='index'),
    path('dashboard/', dashboardPageView, name='dashboard'),
    path('login/', LoginPageView, name='login'),
    path('logout/', LogoutPageView, name='logout'),
    path('metrics/', UserMetricsPageView, name='metrics'),
    path('profile/', ProfilePageView, name='profile'),
    path("showProfile/", showSingleProfilePageView, name="profile_edit"),
    path('edit_profile/', profileEditPageView, name='edit_profile'),
    path('food_add', foodAddPageView, name='food_add'),
    path('food_log_delete/<int:food_id>/', FoodLogDeletePageView, name='food_log_delete'),
    path('', RegisterPageView, name='register'),
]