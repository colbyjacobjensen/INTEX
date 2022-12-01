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

# class User(AbstractUser):
#     def __str__(self):
#         return f'{self.username}'

# class Nutrient(models.Model):
#     nutrient_name = models.CharField(max_length=30)
 
#     class Meta:
#         db_table = 'Nutrient'
 
#     def __str__(self):
#         return (self.nutrient_name)

# class Food(models.Model):
#     food_name = models.CharField(max_length=30)
#     nutrient = models.ManyToManyField(Nutrient, blank=True)
 
#     class Meta:
#         db_table = 'Food'
 
#     def __str__(self):
#         return (self.food_name)

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

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()
    
    # @property
    # def full_name(self):
    #     return '%s %s' % (self.first_name, self.last_name)

# class JournalEntry(models.Model):
#     datetime = models.DateField(default=datetime.today, blank=True)
#     Food = models.ManyToManyField(Food, blank=True)
#     #user = models.ForeignKey(User, on_delete=models.CASCADE)
#     class Meta:
#         db_table = 'Journal Entry'
 
#     def __str__(self):
#         return (str(self.datetime))

# # class Recommendation(models.Model):
# #     class Meta:
# #         unique_together = [('user', 'nutrient')]
# #         db_table = 'Recommendation'

# #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# #     nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
# #     recommended_amount = models.DecimalField(max_digits=8, decimal_places=2)

# class FoodNutrient(models.Model):
#     class Meta:
#         unique_together = [('nutrient', 'food')]
#         db_table = 'Food Nutrient'

#     nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
#     food = models.ForeignKey(Food, on_delete=models.CASCADE)
#     actual_amount = models.IntegerField(default=0)

# class ConsumedFood(models.Model):
#     class Meta:
#         unique_together = [('food', 'journal_entry')]
#         db_table = 'Consumed Food'

#     food = models.ForeignKey(Food, on_delete=models.CASCADE)
#     journal_entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=0)