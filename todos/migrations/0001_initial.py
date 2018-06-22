# Generated by Django 2.0.3 on 2018-06-21 14:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todolist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(max_length=200)),
                ('taskdescription', models.TextField()),
                ('task_document', models.FileField(blank=True, null=True, upload_to='myfolder')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('due_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Worktodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.CharField(max_length=100)),
                ('trywork', models.CharField(max_length=100)),
                ('doing', models.CharField(max_length=200)),
                ('done', models.CharField(max_length=200)),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todos.Todolist')),
            ],
        ),
    ]
