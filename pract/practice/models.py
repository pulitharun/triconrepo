
# Create your models here.
from django.db import models

class UserDetails(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    # Assuming Id is the primary key
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.name