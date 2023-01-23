from django.db import models

# Create your models here.
#el modelo de la bases el esquma para mi base sql 

class Project(models.Model):
     title = models.CharField(max_length=200)
     description= models.TextField()
     technology =models.CharField(max_length=200)
     created_at =models.DateTimeField(auto_now_add=True)
