from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

from django import forms
class RegistrationForm(UserCreationForm):
	class Meta:
		fields = ['username', 'email','first_name','last_name',]
		model = User
