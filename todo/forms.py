from django.forms import ModelForm
from .models import Todo
from django import forms
from django.core.exceptions import NON_FIELD_ERRORS


class AddTodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['name']
        labels = {
            'name' : "Add Todo"
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Add your Todo's here..."}),
        }

