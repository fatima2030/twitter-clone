from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from account.models import profile

class UserRejestrionsForms(UserCreationForm):
    email = forms.EmailField()

    class Meta :
        model = User
        fields = ['username','email','password1']



class UserUpdateForm(forms.ModelForm):

    email = forms.EmailField()

    class Meta :
        model = User
        fields = ['username','email']


class ProfileUpadteForms(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image']
