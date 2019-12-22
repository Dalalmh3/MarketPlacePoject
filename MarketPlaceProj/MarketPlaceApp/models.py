from django.db import models

# Create your models here.
class Product(models.Model):
   pName= models.CharField(max_length=45)
   description = models.TextField()
   img_url = models.ImageField(upload_to ='media/') 
   # created_at = models.DateTimeField(auto_now_add=True)
   # updated_at = models.DateTimeField(auto_now=True)