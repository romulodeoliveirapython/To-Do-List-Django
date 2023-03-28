from django import forms
from todo.models import Tasks
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        exclude = ('user',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password', 'username', 'first_name', 'last_name', 'email', 'date_joined']