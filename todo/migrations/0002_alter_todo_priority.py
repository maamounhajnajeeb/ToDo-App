# Generated by Django 5.0.2 on 2024-02-14 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('Low', 'Low'), ('Med', 'Med'), ('High', 'High')], default='Med', max_length=6),
        ),
    ]
