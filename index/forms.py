from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile


class ModelSignUp(UserCreationForm):

    class Meta:
        model = UserProfile
        # exclude = ['user_type', 'salt']
        # fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',)
        # fields = ('username', 'password')
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }


class ModelEditProfile(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'password')


class UserSignUp(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }), label='Re-enter Password')

    class Meta:
        model = UserProfile
        # exclude = ['user_type', 'salt']
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'autofocus': 'autofocus'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'username': forms.TextInput(attrs={'id': 'user', 'class': 'form-control', 'required': 'required'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'required'}),
            'password': forms.PasswordInput(
                attrs={'class': 'form-control', 'placeholder': 'enter password', 'required': 'required'}
            ),
        }


class UserLogin(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'enter username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'enter password', 'id': 'password'
    }))
