from django import forms
from . models import Todolist,Worktodo

class WorktodoForm(forms.ModelForm):
    priority=forms.ChoiceField(choices=[('low', 'Low'), ('belowlow', 'Belowlow'), ('normal', 'Normal') ,('abovelow'  ,'Abovelow') ,('high' , 'High')])


    class Meta:
        model = Worktodo
        fields = ["todo","priority","trywork","doing","done"]
    '''todo= forms.CtodoharField(max_length=200)
    priority=forms.ChoiceField(choices=[('low', 'Low'), ('belowlow', 'Belowlow'), ('normal', 'Normal') ,('abovelow'  ,'Abovelow') ,('high' , 'High')])
    trywork= forms.CharField(max_length=200)
    doing=forms.CharField(max_length=200)
    done=forms.CharField(max_length=200)'''




class TodolistForm(forms.ModelForm):
    class Meta:
        model =Todolist
        fields=["taskname","taskdescription","task_document","created_at","due_date"]
