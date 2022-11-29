from django.urls import path
from .views import dashboardPageView
from .views import indexPageView
from .views import chartsPageView
from .views import journalPageView

urlpatterns = [
    path('journal/', journalPageView, name='journal'),
    path('charts/', chartsPageView, name='charts'),
    path('index/', indexPageView, name='index'),
    path('', dashboardPageView, name='dashboard'),
]