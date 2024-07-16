from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models  import User


class SignUPform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class ActivateForm(forms.Form):
    code=forms.CharField(max_length=50)
