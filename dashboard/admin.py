from django.contrib import admin
from .models import Profile
from .models import Food
from .models import FoodLog
 
# Register your models here.
admin.site.register(Profile)
admin.site.register(Food)
admin.site.register(FoodLog)