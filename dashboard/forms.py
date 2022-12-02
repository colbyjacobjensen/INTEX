from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .models import Food


# Create your forms here.

class RegisterUserForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control form-control-user'}))
	first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control form-control-user'}))
	last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control form-control-user'}))

	class Meta:
		model = User
		fields = ("username", "first_name", "last_name", "email", "password1", "password2")

	def __init__(self, *args, **kwargs):
		super(RegisterUserForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class'] = 'form-control form-control-user'
		self.fields['username'].widget.attrs['autofocus'] = False
		self.fields['password1'].widget.attrs['class'] = 'form-control form-control-user'
		self.fields['password2'].widget.attrs['class'] = 'form-control form-control-user'

class UserMetricsForm(forms.ModelForm):
	gender = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={'class':'form-control form-control-user'}))
	height_inches = forms.DecimalField(max_digits=8, decimal_places=1, widget=forms.TextInput(attrs={'class':'form-control form-control-user'}))
	weight = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control form-control-user'}))
	age = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control form-control-user'}))

	class Meta:
		model = Profile
		fields = ("gender", "height_inches", "weight", "age")

class FoodForm(forms.ModelForm):
	
	foodName = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={'class':'form-control form-control-user'}))
	calories = forms.DecimalField(widget=forms.TextInput(attrs={'class':'form-control form-control-user'}))
	fatTotal = forms.DecimalField(widget=forms.TextInput(attrs={'class':'form-control form-control-user'}))
	satFat = forms.DecimalField(widget=forms.TextInput(attrs={'class':'form-control form-control-user'}))
	protein = forms.DecimalField(widget=forms.TextInput(attrs={'class':'form-control form-control-user'}))
	sodium = forms.DecimalField(widget=forms.TextInput(attrs={'class':'form-control form-control-user'}))
	potassium = forms.DecimalField(widget=forms.TextInput(attrs={'class':'form-control form-control-user'}))
	cholesterol = forms.DecimalField(widget=forms.TextInput(attrs={'class':'form-control form-control-user'}))
	carbohydrates = forms.DecimalField(widget=forms.TextInput(attrs={'class':'form-control form-control-user'}))
	sugar = forms.DecimalField(widget=forms.TextInput(attrs={'class':'form-control form-control-user'}))
	class Meta:
		model = Food
		fields = ['foodName', 'calories', 'fatTotal', 'satFat', 'protein', 'sodium', 'potassium', 
		'cholesterol', 'carbohydrates', 'sugar']
		
	def __init__(self, *args, **kwargs):
		super(FoodForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'