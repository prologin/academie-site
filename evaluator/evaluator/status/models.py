from django.db import models

class Status(models.Model):
    class Meta:
        managed = False
    
    id = models.UUIDField(primary_key=True)
    status = models.CharField(max_length=150)