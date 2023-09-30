from django.db import models

class CreatedReports(models.Model):
    created = models.DateTimeField(blank=False, null=False, auto_now_add=True)