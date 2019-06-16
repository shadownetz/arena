from django import forms
from .models import (UserProfile, Profile)


class ProfileUpdateForm(forms.ModelForm):
    model = Profile
    exclude = ['user']


class UserUpdateForm(forms.ModelForm):
    model = UserProfile
    exclude = ['is_staff', 'is_active', 'salt', 'avatar', 'date_created', 'is_superuser',]
