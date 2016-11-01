from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from deneme.models import Review
from django import forms
from django.forms import ModelForm

class RegistrationForm(UserCreationForm):
	class Meta:
		fields = ['username', 'email','first_name','last_name',]
		model = User


class ReviewCreationForm(ModelForm):
	class Meta:
		model = Review
		fields = ('comment', 'vote')