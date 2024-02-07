from django import forms

from app.models import *


class user_form(forms.ModelForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username','first_name','last_name','email','password']

        widgets = {'password':forms.PasswordInput()}


class user_profile_form(forms.ModelForm):

    class Meta:
        model = user_profile

        fields = ['profile_pic']


        



