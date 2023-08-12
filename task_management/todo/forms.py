from django import forms
from todo.models import ToDoModel
class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoModel
        fields = ['title','description','status']
        error_messages = {
            'title' : {'required' : 'Title is required'},
            'description' : {'required' : 'Description is required'}
        }