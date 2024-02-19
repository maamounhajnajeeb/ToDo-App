from django.db import models
from django.conf import settings

from core.models import DatesModel


class TaskDates(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    date = models.DateField(null=False, db_index=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ["user", "date"],
                name=" user_date_tasks_constraint",
                ),
            ]
    
    def __str__(self) -> str:
        return f"{self.date.day}/{self.date.month}/{self.date.year}"


class ToDo(DatesModel):
    
    class Priorities(models.TextChoices):
        LOW = ("Low", "Low")
        MED = ("Med", "Med")
        HIGH = ("High", "High")
    
    title = models.CharField(max_length=500, null=False)
    checked = models.BooleanField(default=False, null=False)
    piriority = models.CharField(max_length=6, choices=Priorities.choices, default=Priorities.MED)
    time = models.SmallIntegerField(null=True)
    on_time = models.BooleanField(null=True)
    due_date = models.ForeignKey(TaskDates, on_delete=models.CASCADE, null=False, related_name="related_tasks")
    checked_at = models.DateTimeField(null=True)
    
    def __str__(self):
        return f"{self.title} => Done: {self.checked}"
