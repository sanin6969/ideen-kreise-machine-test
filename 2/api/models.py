from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return self.name