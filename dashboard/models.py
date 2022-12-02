from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Food(models.Model):
    foodName = models.CharField(max_length=200)
    calories = models.IntegerField(default=0)
    fatTotal = models.DecimalField(max_digits=7, decimal_places=2)
    satFat = models.DecimalField(max_digits=7, decimal_places=2)
    protein = models.DecimalField(max_digits=7, decimal_places=2)
    sodium = models.DecimalField(max_digits=7, decimal_places=2)
    potassium = models.DecimalField(max_digits=7, decimal_places=2)
    cholesterol = models.DecimalField(max_digits=7, decimal_places=2)
    carbohydrates = models.DecimalField(max_digits=7, decimal_places=2)
    sugar = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        db_table = 'Food'


    def __str__(self):
        return (self.foodName)

class FoodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Food Log'
        verbose_name_plural = 'Food Log'

    def __str__(self):
        return f'{self.user.username} - {self.food_consumed.foodName}'

class Profile(models.Model):
    gender = models.CharField(max_length=30)
    height_inches = models.DecimalField(max_digits=8, decimal_places=1, default=0)
    weight = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'Metrics'
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)