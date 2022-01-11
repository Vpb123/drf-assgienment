from django.db import models

# Create your models here.
class UserDb(models.Model):
    id= models.PositiveIntegerField(primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    company_name=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=50)
    zip=models.IntegerField()
    email=models.EmailField(max_length=254)
    web=models.URLField()
    age=models.IntegerField()

