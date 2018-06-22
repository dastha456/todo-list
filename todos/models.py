from django.db import models

# Create your models here.

from datetime import datetime
# Create your models here.
class Todolist(models.Model):
    taskname= models.CharField(max_length=200)
    taskdescription=models.TextField()
    task_document=models.FileField(upload_to="myfolder",blank=True,null=True)
    created_at=models.DateTimeField(default=datetime.now, blank=True)
    due_date = models.DateTimeField()

    def __str__(self):
        return self.taskname
class Worktodo(models.Model):
    todo= models.ForeignKey(Todolist,on_delete=models.CASCADE)
    priority= models.CharField(max_length=100)
    trywork = models.CharField(max_length=100)
    doing =  models.CharField(max_length=200)
    done  = models.CharField(max_length=200)
    def __str__(self):
        return self.priority
