from django.db import models


class ToDo(models.Model):
    
    class Priorities(models.TextChoices):
        LOW = ("Low", "Low")
        MED = ("Med", "Med")
        HIGH = ("High", "High")
    
    title = models.CharField(max_length=500, null=False)
    checked = models.BooleanField(default=False, null=False)
    priority = models.CharField(max_length=6, choices=Priorities.choices, default=Priorities.MED)
    time = models.SmallIntegerField(null=True)
    on_time = models.BooleanField(null=True)
