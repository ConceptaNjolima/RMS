from django import forms
from basic_app.models import UserProfileInfo
from django.contrib.auth.models import User


# base form
class Userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password', ]


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        # fields = ['roomNumber', ]
        fields = ['Number']
