from django.db import models

from core.models import DatesModel



class ToDo(DatesModel):
    
    class Priorities(models.TextChoices):
        LOW = ("Low", "Low")
        MED = ("Med", "Med")
        HIGH = ("High", "High")
    
    title = models.CharField(max_length=500, null=False)
    checked = models.BooleanField(default=False, null=False)
    priority = models.CharField(max_length=6, choices=Priorities.choices, default=Priorities.MED)
    time = models.SmallIntegerField(null=True)
    on_time = models.BooleanField(null=True)
    checked_at = models.DateTimeField(null=True)
    
    def __str__(self):
        return f"{self.title} => Done: {self.checked}"
