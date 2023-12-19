from django.db import models

# Create your models here.
class Games(models.Model):
    name =  models.TextField(max_length=50)
    image =  models.ImageField(upload_to='screenshots')
    description =  models.TextField()

    def __str__(self):
        return self.name