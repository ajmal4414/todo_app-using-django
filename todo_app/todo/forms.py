from django import forms
# from django.contrib.auth import login
from django.forms import ModelForm
from .models import Register,Login




# class TaskForm(forms.ModelForm):
#     title=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new task...'}))
#
#     class Meta:
#         model=Tasks
#         fields='__all__'

class RegisterForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
       model= Register
       fields='__all__'

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
       model=Login
       fields=['username','password']

