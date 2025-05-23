from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField()
    author = models.CharField()
    published_date = models.DateField()
    isHit = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title