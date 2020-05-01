from django import forms
from register_app.models import UserProfileInfo
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):

    #validation for the name goes here
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields=('username','first_name','last_name','email','password')

class UserProfileInfoForm(forms.ModelForm):

    ##validation for fields under UserProfileInfo

    class Meta:
        model=UserProfileInfo
        fields=("portfolio_link","profile_pic")
