from django import forms
from django.contrib.auth.models import User
from pratikapp.models import Task

class Userform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']


class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields='__all__'
