# Generated by Django 5.0.2 on 2024-02-14 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todo_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='created_at',
        ),
    ]
