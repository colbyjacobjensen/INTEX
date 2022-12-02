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

    # add other fields here
	class Meta:
		model = User
		fields = ("username", "first_name", "last_name", "email", "password1", "password2")

	def __init__(self, *args, **kwargs):
		super(RegisterUserForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class'] = 'form-control form-control-user'
		self.fields['username'].widget.attrs['autofocus'] = False
		self.fields['password1'].widget.attrs['class'] = 'form-control form-control-user'
		self.fields['password2'].widget.attrs['class'] = 'form-control form-control-user'

	# def save(self, commit=True):
	# 	user = super(RegisterUserForm, self).save(commit=False)
	# 	# user.gender = self.cleaned_data['gender']
	# 	# user.height_inches = self.cleaned_data['height_inches']
	# 	# user.weight = self.cleaned_data['weight']
	# 	# user.age = self.cleaned_data['age']
	# 	# user.stage = self.cleaned_data['stage']

	# 	if commit:
	# 		user.save()
	# 	return user

# GENDER_OPTIONS= ['Male', 'Female']

class UserMetricsForm(forms.ModelForm):
	# gender = forms.CharField(max_length = 50, widget=forms.Select(attrs={'class':'form-control form-control-user'}, choices=GENDER_OPTIONS))
	gender = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={'class':'form-control form-control-user'}))
	height_inches = forms.DecimalField(max_digits=8, decimal_places=1, widget=forms.TextInput(attrs={'class':'form-control form-control-user'}))
	weight = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control form-control-user'}))
	age = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control form-control-user'}))

	class Meta:
		model = Profile
		fields = ("gender", "height_inches", "weight", "age")

# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control form-control-user'}))

#     class Meta:
#         model = User 
#         fields = ['username', 'email']

# class ProfileUpdateForm(forms.ModelForm):
#     city = forms.CharField(label='City', max_length=100)
#     state = forms.CharField(label='State', required=False, max_length=50)
#     country = forms.CharField(label='Country (if outside U.S.)', required=False, max_length=100)
#     favorite_artists = forms.CharField(label='Your favorite artists (use commas)', required=False, max_length=200)
#     about_user = forms.CharField(widget=forms.Textarea(attrs={"rows": 7}), label='A small description of yourself', required=False)

# class Meta:
#     model = Profile
#     fields = ['city', 'state', 'country', 'favorite_artists', 'about_user']

    # class UserCreateForm(UserCreationForm):
    # extra_field = forms.CharField(required=True)

    # class Meta:
    #     model = User
    #     fields = ("username", "extra_field", "password1", "password2")

    # def save(self, commit=True):
    #     user = super(UserCreateForm, self).save(commit=False)
    #     user.extra_field = self.cleaned_data["extra_field"]
    #     if commit:
    #         user.save()
    #     return user

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