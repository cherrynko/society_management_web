from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from User.models import DEPARTMENTS,ROLES
# from django.contrib.auth import get_user_model
# from .models import CustomUser

from django.contrib.auth import get_user_model


User = get_user_model()

class Recruit(UserCreationForm):
    department = forms.ChoiceField(choices=DEPARTMENTS)
    role = forms.ChoiceField(choices=ROLES)
    email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
    password=forms.CharField(label="Password",max_length=50,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    
    class Meta:
        model = User
        fields = ['first_name','last_name', 'department', 'role', 'email', 'username','password']
