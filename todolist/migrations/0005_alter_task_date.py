# Generated by Django 4.1 on 2022-09-27 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_alter_task_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
