from django import forms
from todo.models import Tasks


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        exclude = ('user',)
