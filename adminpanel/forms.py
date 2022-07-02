from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class Forma(UserCreationForm):
    username = forms.CharField(max_length = 50,label='username')
    email = forms.CharField(max_length=50,label='email')

    class Meta:
        model = User
        fields = ('username','email')


