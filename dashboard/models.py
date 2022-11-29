from django.db import models
from datetime import datetime
# Create your models here.
class Nutrient(models.Model):
    nutrient_name = models.CharField(max_length=30)
 
    class Meta:
        db_table = 'Nutrient'
 
    def __str__(self):
        return (self.nutrient_name)

class Food(models.Model):
    food_name = models.CharField(max_length=30)
    nutrient = models.ManyToManyField(Nutrient, blank=True)
 
    class Meta:
        db_table = 'Food'
 
    def __str__(self):
        return (self.food_name)

class User(models.Model):
    email = models.EmailField(max_length=100)    
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    height_inches = models.DecimalField(max_digits=8, decimal_places=1, default=0)
    weight = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    stage = models.CharField(max_length=30, blank=True)
    comorbidity_type = models.CharField(max_length=30, blank=True)

    class Meta:
        db_table = 'User'
 
    def __str__(self):
        return (self.full_name)
    
    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

class JournalEntry(models.Model):
    datetime = models.DateField(default=datetime.today, blank=True)
    Food = models.ManyToManyField(Food, blank=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'Journal Entry'
 
    def __str__(self):
        return (str(self.datetime))

class Recommendation(models.Model):
    class Meta:
        unique_together = [('user', 'nutrient')]
        db_table = 'Recommendation'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
    recommended_amount = models.DecimalField(max_digits=8, decimal_places=2)

class FoodNutrient(models.Model):
    class Meta:
        unique_together = [('nutrient', 'food')]
        db_table = 'Food Nutrient'

    nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    actual_amount = models.IntegerField(default=0)

class ConsumedFood(models.Model):
    class Meta:
        unique_together = [('food', 'journal_entry')]
        db_table = 'Consumed Food'

    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    journal_entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)