from django.contrib import admin

# Register your models here.
from . models import Todolist,Worktodo

admin.site.register(Todolist)
admin.site.register(Worktodo)
