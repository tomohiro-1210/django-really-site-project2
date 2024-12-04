from django import forms
from django.contrib.auth import get_user_model
from mysiteapp.models.profile_models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'zipcode', 'prefecture', 'city', 'address')
        