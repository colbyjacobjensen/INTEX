from django.contrib import admin
from .models import Profile
from .models import Food
from .models import FoodLog
#from .models import JournalEntry
#from .models import Nutrient
#from .models import Recommendation
#from .models import ConsumedFood
 
# Register your models here.
admin.site.register(Profile)
admin.site.register(Food)
admin.site.register(FoodLog)
#admin.site.register(JournalEntry)
#admin.site.register(Nutrient)
#admin.site.register(Recommendation)
#admin.site.register(ConsumedFood)