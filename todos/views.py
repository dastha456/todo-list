from django.shortcuts import render,redirect
from . models import Todolist, Worktodo
# Create your views here.
from . forms import WorktodoForm,TodolistForm

def home(request):
    form =Todolist.objects.all()
    form1 =Worktodo.objects.all()
    context={
    "todo1" : form,
    "todo2" : form1,
    }
    return render(request, 'home.html', context)
def todocreate(request):
    if request.method=="POST":
         form = TodolistForm(request.POST or None)
         if form.is_valid():
             form.save()

         return redirect('/todos/workcreate/')
    else:
        allitems=TodolistForm()
        return render(request,'index.html', {"todo1":allitems})

def worktodocreate(request):
    if request.method=="POST":
        form = WorktodoForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('/todos/')
    else:
        allitem =WorktodoForm()
        return render(request,'workindec.html',{"todo2":allitem})

def details(request, id):
    obj=Todolist.objects.get(id=id)
    obj1= Worktodo.objects.get(todo =todos)
    context={
    "todo1":obj,
    "todo2":obj1,
    }
    return render(request,'details.html',context)
