from django.db import models

# Create your models here.

class Contractor(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    budget = models.IntegerField(default=100)
    job_start_time = models.IntegerField(default=100)
    pickup_available = models.BooleanField()
    contact_info = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
        