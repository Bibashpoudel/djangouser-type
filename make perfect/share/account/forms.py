from django import forms
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()



class SponsorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_sponsor = True
        if commit:
            user.save()
        return user


class IdeapeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

        

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_ideapeacher = True
        if commit:
            user.save()
        return user