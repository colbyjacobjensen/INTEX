from django.contrib import admin
from .models import User
from .models import Food
from .models import JournalEntry
from .models import Nutrient
from .models import Recommendation
from .models import FoodNutrient
from .models import ConsumedFood
 
# Register your models here.
admin.site.register(User)
admin.site.register(Food)
admin.site.register(JournalEntry)
admin.site.register(Nutrient)
admin.site.register(Recommendation)
admin.site.register(FoodNutrient)
admin.site.register(ConsumedFood)