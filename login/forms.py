from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
#from .models import our_users


class CreateUserForm(UserCreationForm):
	class Meta:
		model=User
		fields =['username','email','password1','password2']


# save users where know
"""
class save_user(forms.ModelForm):
	class Meta:
		model=our_users
		fields=['username','email']
		"""