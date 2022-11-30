from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import Food


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
		self.fields['password1'].widget.attrs['class'] = 'form-control form-control-user'
		self.fields['password2'].widget.attrs['class'] = 'form-control form-control-user'

	# def save(self, commit=True):
	# 	user = super(RegisterUserForm, self).save(commit=False)
	# 	user.email = self.cleaned_data['email']
	# 	if commit:
	# 		user.save()
	#     return user


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
    class Meta:
        # model = Food
        fields = '__all__'