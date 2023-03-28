from django import forms
from todo.models import Tasks


class ToDoForm(forms.ModelForm):
    class Meta:
        model = Tasks
        exclude = ('user',)
