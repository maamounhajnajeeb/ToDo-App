from django.db import models


class DatesModel(models.Model):
	created_at = models.DateTimeField(null=False, auto_now_add=True)
	
	class Meta:
		abstract = True
